<!--src/views/WebContact.vue-->

<template>
    <WebHeader />
    <main class="flex-position">
        <section class="service-header">
            <h1>
                Contact Us
            </h1>
            <br>
            <p>
                Have any questions or need assistance? Feel free to leave a message in the form below, and we will get
                back to you as soon as possible. Thank you!
            </p>
        </section>
        <div class="contact">
            <form @submit.prevent="submitForm">
                <label for="name">Name*:</label>
                <input 
                    type="text" 
                    id="name" 
                    v-model="formData.name" 
                    class="regular-input" 
                    placeholder="Enter your name." 
                    required
                />
                <label for="email">Email*:</label>
                <input 
                    type="email" 
                    id="email" 
                    v-model="formData.email" 
                    class="regular-input" 
                    placeholder="Enter your email." 
                    required
                >
                <label for="issue">Type of Issue*</label>
                <select 
                    id="issue" 
                    v-model="formData.issue" 
                    class="regular-select" 
                    required
                >
                    <option value="">Select an issue</option>
                    <option value="issue1">Operational Issues</option>
                    <option value="issue2">Bug Report</option>
                    <option value="issue3">Feature Request</option>
                </select>
                <label for="message">Message*:</label>
                <textarea 
                    id="message" 
                    v-model="formData.message" 
                    placeholder="Enter your message." 
                    required
                ></textarea>
                <button type="submit" class="process-button">Send</button>
            </form>
        </div>
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
            formData: {
                name: '',
                email: '',
                issue: '',
                message: ''
            }
        };
    },
    methods: {
        submitForm() {
            console.log("Form submitted: ", this.formData);
            this.formData = {
                name: '',
                email: '',
                issue: '',
                message: ''
            };
        }
    },
    components: {
        WebHeader
    }
};
</script>

<style>
.flex-position {
    padding-top: 80px;
    justify-content: center;
    align-items: center;
}

.contact {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 50%;
    max-width: 600px;
    margin: 0 auto;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #07334b;
}

.regular-input,
.regular-select,
textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

input::placeholder,
textarea::placeholder {
    color: #bbb;
}

textarea {
    resize: vertical;
    min-height: 100px;
}
</style>