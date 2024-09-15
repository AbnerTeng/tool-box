import os
from jinja2 import Environment, FileSystemLoader

# Set up directories
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'app', 'templates')
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'app', 'static')
BUILD_DIR = os.path.join(os.path.dirname(__file__), 'docs')

# Ensure build directory exists
if not os.path.exists(BUILD_DIR):
    os.makedirs(BUILD_DIR)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
PREFIX_URL = 'https://abnerteng.github.io/tool-box'

class MockRequest:
    def url_for(self, name, **params):
        # Mocking the FastAPI's url_for behavior
        if name == 'static':
            filename = params.get('filename', '')
            return f'static/{filename}'
        else:
            # For other routes, you may need to define how the URLs should look like
            return f'{PREFIX_URL}/{name}'

mock_request = MockRequest()


def url_for_prefixed(request, name, **params):
    """
    Generate a URL for the given endpoint with optional prefixing.
    """
    if name == 'static':
        filename = params.get('filename', '')
        return f'static/{filename}'

    url = request.url_for(name, **params)
    return f'{url}'


def render_template(template_name, **context):
    """
    Render a Jinja2 template and return it as a string.
    """
    context['request'] = mock_request
    context['url_for_prefixed'] = url_for_prefixed
    template = env.get_template(template_name)
    return template.render(**context)

def save_html(output_path, content):
    """
    Save the rendered HTML content to the output path.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def build_site():
    """
    Build the static site by rendering templates and saving them as static HTML files.
    """
    pages = [
        ('index.html', '/index.html'),
        # ('log_in.html', '/log_in.html'),
        # ('sign_up.html', '/sign_up.html'),
        ('about.html', '/about.html'),
        ('contact.html', '/contact.html'),
        ('img_proc.html', '/service1.html'),
        ('email_sender.html', '/service2.html'),
        ('email_temp.html', '/service2_templates.html'),
    ]

    for template_name, _ in pages:
        # Render the template
        html_content = render_template(template_name)

        # Define the output path
        output_path = os.path.join(BUILD_DIR, template_name)

        # Save the rendered HTML to a file
        save_html(output_path, html_content)
        print(f"Generated: {output_path}")

if __name__ == '__main__':
    build_site()
