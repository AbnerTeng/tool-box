<!--src/views/EmailTemp.vue-->

<template>
    <WebHeader />
    <main class="flex-position">
        <section class="service-header">
            <h1>Template Preview</h1>
        </section>
        <dev class="tabs">
            <div class="tab active">Member Recruiting</div>
            <div class="tab">Director Recruiting</div>
            <div class="tab">Corporate Visiting</div>
        </dev>
        <div class="carousel">
            <button class="carousel-control prev">&lt;</button>
            <div class="carousel-md">
                <div id="content-display">
                    <p>Temp</p>
                </div>
            </div>
            <button class="carousel-control next">&gt;</button>
        </div>
        <div class="markdown-input">
            <div class="toolbar">
                <button class="toolbar-btn" data-md="**" title="Bold"><b>B</b></button>
                <button class="toolbar-btn" data-md="*" title="Italic"><i>I</i></button>
                <button class="toolbar-btn" data-md="#" title="Heading">H1</button>
                <button class="toolbar-btn" data-md="##" title="Subheading">H2</button>
                <button class="toolbar-btn" data-md="###" title="Subheading">H3</button>
                <button class="toolbar-btn" data-md="- " title="List">List</button>
                <button class="toolbar-btn" data-md="[Link](url)" title="URL">Link</button>
                <button class="toolbar-btn" data-md="`" title="Inline Code">Code</button>
                <button class="toolbar-btn" data-md="```\n" title="Code Block">Code Block</button>
            </div>
            <div class="editor-area">
                <textarea id="markdown-editor" rows="10" cols="50" placeholder="Type your markdown here"></textarea>
                <div id="markdown-preview" class="markdown-preview"></div>
            </div>
        </div>
    </main>
</template>

<script>
import WebHeader from '@/components/WebHeader.vue';
import { marked } from 'marked';

export default {
    components: {
        WebHeader
    },
    data() {
        return {
            tabs: ['Tab1', 'Tab2', 'Tab3'],
            markdownText: '',
            contents: [
                "<h2>Welcome to Member Recruiting</h2><p>This is a paragraph of HTML content. You can add more HTML here.</p>",
                "### Director Recruiting\n- Director 1\n- Director 2\n- Director 3",
                "<p><strong>Corporate Visiting:</strong> This section will provide all the details about corporate visits.</p>"
            ],
            currentIndex: 0,
            displayOriginal: false,
        };
    },
    mounted() {
        this.updateMarkdownPreview();
        this.renderContent(this.contents[this.currentIndex]);
        this.initEventListeners();
    },
    methods: {
        initEventListeners() {
            const tabs = document.querySelectorAll('.tab');
            const markdownEditor = document.getElementById('markdown-editor');
            const toolbarButtons = document.querySelectorAll('.toolbar-btn');
    
            tabs.forEach((tab, index) => {
                tab.addEventListener('click', () => {
                    tabs.forEach(t => t.classList.remove('active'));
                    tab.classList.add('active');
                    this.currentIndex = index;
                    this.displayOriginal = false;
                    this.renderContent(this.contents[this.currentIndex]);
                });
            });
            document.querySelector('.next').addEventListener('click', () => {
                this.displayOriginal = true;
                this.renderContent(this.contents[this.currentIndex]);
            });

            document.querySelector('.prev').addEventListener('click', () => {
                this.displayOriginal = false;
                this.renderContent(this.contents[this.currentIndex]);
            });

            toolbarButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const markdownSyntax = button.getAttribute('data-md');
                    this.insertMarkdown(markdownEditor, markdownSyntax);
                });
            });
            markdownEditor.addEventListener('input', this.updateMarkdownPreview);
        },
        renderContent(content) {
            const contentDisplay = document.getElementById('content-display');
            if (this.displayOriginal) {
                contentDisplay.innerText = content;
            } else {
                contentDisplay.innerHTML = marked.parse(content);
            }
        },
        insertMarkdown(textarea, syntax) {
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
            this.updateMarkdownPreview();
        },
        updateMarkdownPreview() {
            const markdownEditor = document.getElementById('markdown-editor');
            const markdownPreview = document.getElementById('markdown-preview');
            const markdownText = markdownEditor.value;

            markdownPreview.innerHTML = marked.parse(markdownText);
        }
    }
}
</script>

<style>
.flex-position {
    justify-content: center;
    align-items: center;
}

.tabs {
    display: flex;
    justify-content: center;
    background-color: #fff;
    padding: 20px 0;
    /* border-bottom: 2px solid #ddd; */
    margin-bottom: 20px;
}

.tab {
    margin: 0 20px;
    padding: 10px 20px;
    cursor: pointer;
    color: #333;
}

.tab.active {
    color: #07334b;
    border-bottom: 3px solid #07334b;
    font-weight: bold;
}

.carousel {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 60%;
    margin: 0 auto;
    position: relative;
    background-color: #f5f5f5;
    padding: 40px;
    border-radius: 10px;
    flex-direction: row;
}

.carousel-md {
    width: 100%;
    padding: 20px;
    border-radius: 10px;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px;
}

.content-display {
    max-width: 100%;
    text-align: center;
}

.carousel-control {
    background-color: #fff;
    border: none;
    font-size: 24px;
    cursor: pointer;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    padding: 10px;
    border-radius: 50%;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}

.carousel-control.prev {
    left: 10px;
    width: 50px;
    height: 50px;
}

.carousel-control.next {
    right: 10px;
    width: 50px;
    height: 50px;
}

.markdown-input {
    display: flex;
    /* align-items: center; */
    width: 100%;
    margin-top: 20px;
    flex-direction: column;
}

.toolbar {
    display: flex;
    gap: 5px;
    margin-bottom: 10px;
    flex-direction: row;
}

.toolbar-btn {
    padding: 5px 10px;
    cursor: pointer;
    background-color: #07334b;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 14px;
}

.toolbar-btn:hover {
    background-color: #07334b;
}

/* Editor Area */
.editor-area {
    display: flex;
    gap: 20px;
}

#markdown-editor {
    width: 50%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    resize: vertical;
    height: 300px;
}

.markdown-preview {
    width: 50%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
    overflow-y: auto;
    height: 300px;
}
</style>