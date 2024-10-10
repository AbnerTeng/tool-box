<!--src/views/ImgProc.vue-->

<template>
    <WebHeader />
    <main class="flex-position">
        <section id="grcode-gen">
            <dev class="service-header">
                <h1>Image Processor</h1>
            </dev>
            <div class="method">
                <h1>QRCode Generator</h1>
                <p>
                    Generate QR codes online by entering your desired URL and clicking the "Process" button.
                    It's a simple and quick way to create scannable codes for easy sharing and access.
                </p>
                <div class="input">
                    <form submit.prevent="generateQRCode">
                        <div id="urlInput">
                            <label for="url" class="big-label">Enter URL: </label>
                            <input type="text" v-model="url" id="url" class="regular-input"
                                placeholder="Enter your URL." required />
                        </div>
                        <button type="submit" class="process-button">Process</button>
                    </form>
                </div>
            </div>
        </section>
        <section id="bg-remove">
            <div class="method">
                <h1>Background Remover</h1>
                <p>
                    Quickly and easily remove backgrounds from images. Simply upload your image and click the "Process"
                    button to get a clean, background-free result.
                </p>
                <div class="input">
                    <form submit.prevent="removeBackground">
                        <div id="imageUpload">
                            <label for="bgRemoveImage" class="big-label">Upload an Image: </label>
                            <input type="file" ref="bgRemoveImage" class="choose-input" accept=".jpeg .jpg .png" required/>
                        </div>
                        <button type="submit" class="process-button">Process</button>
                    </form>
                </div>
            </div>
        </section>
        <section id="heic2jpg">
            <div class="method">
                <h1>.HEIC to .jpg</h1>
                <p>
                    Quickly and easily transfer .HEIC type .jpg from images. Simply upload your image and click the
                    "Process" button to get a converted .jpg file.
                </p>
                <div class="input">
                    <form submit.prevent="convertHEICtoJPG">
                        <div id="imageUpload" v-show="true">
                            <label for="heicImage" class="big-label">Upload an Image: </label>
                            <input type="file" ref="heicImage" class="choose-input" accept=".heic" required/>
                        </div>
                        <button type="submit" class="process-button">Process</button>
                    </form>
                </div>
            </div>
        </section>
    </main>
    <div class="short-thick-line"></div>
    <footer class="bottom-text">
        <p>© 2024 Tool-Box</p>
    </footer>
</template>

<script>
import WebHeader from '@/components/WebHeader.vue';

export default {
    data() {
        return {
            url: ''
        };
    },
    methods: {
        generateQRCode() {
            console.log('Generating QR code for URL:', this.url);
        },
        removeBackground() {
            const image = this.$refs.bgRemoveImage.files[0];
            console.log('Removing background from image:', image.name);
        },
        convertHEICtoJPG() {
            const image = this.$refs.heicImage.files[0];
            console.log('Converting .HEIC to .jpg:', image.name);
        }
    },
    components: {
        WebHeader
    }
};
</script>
<style>
.flex-position {
    justify-content: center;
    align-items: center;
}

.method {
    width: 50%;
    margin: 50px 150px;
}

.method h1 {
    font-size: 30px;
    font-weight: bold;
    color: #07334b;
}

.input {
    display: flex;
    justify-content: left;
    align-items: left;
    margin-top: 50px;
}

.big-label {
    font-size: 20px;
    font-weight: bold;
    color: #07334b;
    margin-right: 10px;
}

.process-button {
    background-color: #07334b;
    border: none;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.choose-input {
    width: 300px;
    height: 30px;
    margin-right: 10px;
    font-size: 16px;
    border: none;
}

.regular-input,
.regular-select {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}
</style>