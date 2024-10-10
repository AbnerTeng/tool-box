<!--src/views/WebHome.vue-->

<template>
    <div>
        <WebHeader />
        <main class="flex-main">
            <section class="main-text">
                <h1>Accelerate<br>
                    Your Productivity
                </h1>
                <p>
                    Frustrated by the repetitive tasks? Tool Box unlocks the potential of your efficiency of
                    administrative
                    work.
                </p>
            </section>
            <div class="horizontal-line"></div>
            <section class="service-header">
                <h1>Our Services</h1>
            </section>
            <div class="container">
                <div class="content-service">
                    <h2>Say Goodbye to force signup websites</h2>
                    <p>
                        Image processing utilities like generating QR codes and removing backgrounds are now available
                        without any signup. No more wasting time on forced signup websites.
                    </p>
                    <div class="explore-container">
                        <router-link class="explore" to="/img_proc" role="button" tabindex="0">
                            Explore Image Processor
                        </router-link>
                        <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M5 12h14m-6-6l6 6-6 6" stroke="#1F9CDA" stroke-width="2" fill="none"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                </div>
                <div class="content-service">
                    <h2>Achieve FULL automation on operation</h2>
                    <p>
                        The fully automated email sender can send large amounts of emails at once and customize the
                        content of each email using Markdown-like syntax.
                    </p>
                    <div class="explore-container">
                        <router-link class="explore" to="/email_sender" role="button" tabindex="0">
                            Explore Auto Email Sender
                        </router-link>
                        <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M5 12h14m-6-6l6 6-6 6" stroke="#1F9CDA" stroke-width="2" fill="none"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                </div>
            </div>
        </main>
        <div class="short-thick-line"></div>
        <footer class="bottom-text">
            <p>© 2024 Tool-Box</p>
        </footer>
    </div>
</template>

<script>
import WebHeader from '@/components/WebHeader.vue';

export default {
    components: {
        WebHeader
    }
};
</script>

<style>
.flex-main {
    padding-top: 10px;
}

.main-text {
    text-align: left;
    margin: 50px 150px;
    width: 40%;
    color: #07334b;
}

.main-text h1 {
    font-size: 42px;
    font-weight: bold;
    color: #07334b;
}

.main-text p {
    font-size: 18px;
    color: #07334b;
    margin-top: 20px;
    letter-spacing: 0.5px;
    line-height: 1.5;
}

.container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: 50px 150px;
}

.content-service {
    text-align: center;
    width: 80%;
    max-width: 600px;
    margin: 30px 30px;
    box-sizing: border-box;
}

.content-service h2 {
    font-size: 26px;
    font-weight: bold;
    color: #07334b;
}

.content-service p,
.method p {
    text-align: left;
    color: #07334b;
}

.explore-container {
    display: flex;
    justify-content: center;
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
</style>