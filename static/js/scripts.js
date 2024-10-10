document.querySelectorAll('input[name="action"]').forEach(function (radio) {
    radio.addEventListener('change', function () {
        if (this.value === 'remove_background') {
            document.getElementById('imageUpload').style.display = 'block';
            document.getElementById('urlInput').style.display = 'none';
            document.getElementById('eventSelect').style.display = 'none';
            document.getElementById('receiverUpload').style.display = 'none';
        } else if (this.value === 'generate_qrcode') {
            document.getElementById('imageUpload').style.display = 'none';
            document.getElementById('urlInput').style.display = 'block';
            document.getElementById('eventSelect').style.display = 'none';
            document.getElementById('receiverUpload').style.display = 'none';
        } else {
            document.getElementById('imageUpload').style.display = 'none';
            document.getElementById('urlInput').style.display = 'none';
            document.getElementById('eventSelect').style.display = 'block';
            document.getElementById('receiverUpload').style.display = 'block';
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const tabs = document.querySelectorAll('.tab');
    const contentDisplay = document.getElementById('content-display');
    const markdownEditor = document.getElementById('markdown-editor');
    const markdownPreview = document.getElementById('markdown-preview');
    const toolbarButtons = document.querySelectorAll('.toolbar-btn');

    const contents = [
        "<h2>Welcome to Member Recruiting</h2><p>This is a paragraph of HTML content. You can add more HTML here.</p>",  // HTML content
        "### Director Recruiting\n- Director 1\n- Director 2\n- Director 3",  // Markdown content
        "<p><strong>Corporate Visiting:</strong> This section will provide all the details about corporate visits.</p>"  // HTML content
    ];
    let currentIndex = 0;
    let displayOriginal = false;

    renderContent(contents[currentIndex]);

    tabs.forEach((tab, index) => {
        tab.addEventListener('click', function () {
            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            currentIndex = index;
            displayOriginal = false;
            renderContent(contents[currentIndex]);
        });
    });

    document.querySelector('.next').addEventListener('click', function () {
        displayOriginal = true;
        renderContent(contents[currentIndex]);
    });

    document.querySelector('.prev').addEventListener('click', function () {
        displayOriginal = false;
        renderContent(contents[currentIndex]);
    });

    toolbarButtons.forEach(button => {
        button.addEventListener('click', function () {
            const markdownSyntax = this.getAttribute('data-md');
            insertMarkdown(markdownEditor, markdownSyntax);
        });
    });

    function renderContent(content) {
        if (displayOriginal) {
            contentDisplay.innerText = content;
        }
        else {
            contentDisplay.innerHTML = marked.parse(content);
        }
    }

    function insertMarkdown(textarea, syntax) {
        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        const text = textarea.value;
        const selectedText = text.substring(start, end);

        let updatedText;
        if (syntax === '[Link](url)') {
            updatedText = `[${selectedText || 'Link Text'}](url)`;
        } else if (syntax === '```\n') {
            updatedText = `\`\`\`\n${selectedText}\n\`\`\``;
        } else if (syntax === '#' || syntax === '##' || syntax === '###' || syntax === '-') {
            updatedText = `${syntax} ${selectedText}`;
        } else {
            updatedText = `${syntax}${selectedText}${syntax}`;
        }

        textarea.value = text.substring(0, start) + updatedText + text.substring(end);
        textarea.focus();
        textarea.setSelectionRange(start + syntax.length, end + syntax.length);

        updateMarkdownPreview();
    }

    markdownEditor.addEventListener('input', updateMarkdownPreview);

    function updateMarkdownPreview() {
        const markdownText = markdownEditor.value;
        markdownPreview.innerHTML = marked.parse(markdownText);
    }

    updateMarkdownPreview();
});