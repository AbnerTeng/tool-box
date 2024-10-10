<!--src/views/EmailSender.vue-->

<template>
    <WebHeader />
    <main class="flex-position">
        <section id="mail-sender">
            <div class="service-header">
                <h1>Auto Email Sender</h1>
            </div>
            <div class="method">
                <h1>Auto Email Sender</h1>
                <div class="instructions">
                    <h2>Instruction</h2>
                    <p>Here are the steps to automatically send emails</p>
                    <br>
                    <p>Step 1: Select the event you want to send emails for</p>
                    <p>Step 2: Upload the receivers' data in the below format (make sure they are stored in a
                        <b> .csv </b>file!)
                    </p>
                    <p>Step 3: Input links you want to insert in the mail content</p>
                    <p>Step 4: Input the mail subject (Ex: 第五屆 NTUDAC 社員招募 | 個人面試時間通知)</p>
                    <p>
                        Step 5: Type the sender's email and password (
                        <a
                            href="https://shinher.gitbook.io/shinher/ru-he-shen-qing-ying-yong-cheng-shi-zhuan-yong-mi-ma">
                            How to get the password?
                        </a>
                        )
                    </p>
                    <div class="explore-temp-container">
                        <router-link class="explore" to="/email_temp" role="button" tabindex="0">
                            Template Review
                        </router-link>
                        <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M5 12h14m-6-6l6 6-6 6" stroke="#1F9CDA" stroke-width="2" fill="none"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                </div>
                <div class="input">
                    <form @submit.prevent="sendEmail">
                        <label for="event" class="big-label">Select Event: </label>
                        <select 
                            id="event"
                            v-model="formData.event"
                            class="regular-select"
                            required
                        >
                            <option value="">Select an event</option>
                            <option value="event1">Member Recruiting</option>
                            <option value="event3">Director Recruting</option>
                            <option value="event3">Corporate Visiting</option>
                            <option value="event4">To be continue...</option>
                        </select>
                        <br>
                        <label for="receiver" class="big-label">Upload the receiver list: </label>
                        <input 
                            type="file"
                            ref="csvReceiver"
                            id="receiver"
                            class="choose-input"
                            accept=".csv"
                            @change="handleFileUpload"
                            required
                        >
                        <br>
                        <label for="addlinks" class="big-label">Enter Additional Links: </label>
                        <input
                            type="text"
                            id="addlinks"
                            v-model="formData.addlinks"
                            class="regular-input"
                            placeholder="Enter Additional Links"
                        >
                        <br>
                        <label for="subject" class="big-label">Enter Mail Subject: </label>
                        <input 
                            type="text"
                            id="subject"
                            v-model="formData.subject"
                            class="regular-input"
                            placeholder="Enter Mail Subject"
                            required
                        >
                        <br>
                        <label for="email" class="big-label">Enter Email: </label>
                        <input
                            type="text"
                            id="email"
                            v-model="formData.email"
                            class="regular-input"
                            placeholder="Enter Email"
                            required
                        >
                        <br>
                        <label for="password" class="big-label">Enter Password: </label>
                        <input 
                            type="password"
                            id="password"
                            v-model="formData.password"
                            class="regular-input"
                            placeholder="Enter Password"
                            required
                        >
                        <button type="submit" class="process-button">Send</button>
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
    name: 'EmailSender',
    components: {
        WebHeader
    },
    data() {
        return {
            formData: {
                event: '',
                addlinks: '',
                subject: '',
                email: '',
                password: ''
            }
        };
    },
    methods: {
        sendEmail() {
            console.log('Email sent', this.formData);
            this.formData = {
                event: '',
                addlinks: '',
                subject: '',
                email: '',
                password: ''
            };
        },
        handleFileUpload() {
            const fileInput = this.$refs.csvReceiver;
            if (fileInput && fileInput.files.length > 0) {
                const csv = fileInput.files[0];
                console.log('Uploading receiver list:', csv.name);
            } else {
                console.error('No file selected');
            }
        }
    },
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
    text-align: left;
}

.method h1 {
    font-size: 30px;
    font-weight: bold;
    color: #07334b;
}

.instructions {
    margin-top: 20px;
}

.instructions h2 {
    font-size: 24px;
    font-weight: bold;
    color: #07334b;
}

.instructions p {
    font-size: 16px;
    color: #07334b;
    margin-top: 20px;
    line-height: 1.2;
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

.explore-temp-container {
    display: flex;
    justify-content: left;
    align-items: center;
    text-align: center;
    margin-top: 20px;
}

.explore {
    display: inline-flex;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1F9CDA;
    transition: 0.4s;
    align-items: center;
    text-decoration: none;
    text-align: center;
    margin: 4px 4px;
}

.explore:hover {
    opacity: 0.7;
}

.regular-input,
.regular-select {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

.choose-input {
    width: 300px;
    height: 30px;
    margin-right: 10px;
    font-size: 16px;
    border: none;
}
</style>