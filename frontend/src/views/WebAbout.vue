<!--src/views/WebAbout.vue-->

<template>
    <WebHeader />
    <main class="flex-position">
        <section class="service-header">
            <h1>
                We dedicate to create something useful and cool.
            </h1>
        </section>
        <div class="flex-info">
            <div class="person">
                <div class="person-img">
                    <img :src="dev1">
                    <div class="overlay">
                        <div class="icon-button">
                            <a href="https://www.linkedin.com/in/yu-chen-abner" target="_blank">
                                <img :src="linkedinIcon" alt="LinkedIn" class="linkedin-icon">
                            </a>
                        </div>
                    </div>
                </div>
                <div class="person-info">
                    <h3>Yu-Chen Den</h3>
                    <p>Full-Stack Engineer</p>
                </div>
            </div>
            <div class="person">
                <div class="person-img">
                    <img :src="pm1">
                    <div class="overlay">
                        <div class="icon-button">
                            <a href="https://www.linkedin.com/in/carol09144" target="_blank">
                                <img :src="linkedinIcon" alt="LinkedIn" class="linkedin-icon">
                            </a>
                        </div>
                    </div>
                </div>
                <div class="person-info">
                    <h3>Yu-Lin Zheng</h3>
                    <p>Project Manager</p>
                </div>
            </div>
        </div>
    </main>
    <div class="short-thick-line"></div>
    <footer class="bottom-text">
        <p>© 2024 Tool-Box</p>
    </footer>
</template>

<script>
import WebHeader from '@/components/WebHeader.vue';
import dev1 from '@/assets/images/Abner.jpg';
import pm1 from '@/assets/images/carol.jpg';
import linkedinIcon from '@/assets/images/linkedin.jpg';

export default {
    data() {
        return {
            dev1,
            pm1,
            linkedinIcon
        };
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

.flex-info {
    display: flex;
    justify-content: center;
    flex-direction: row;
    width: 100%;
    padding: 20px;
}

.person {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.person-img {
    position: relative;
    margin: 20px;
    width: 150px;
    text-align: center;
    flex-shrink: 0;
    box-sizing: border-box;
}

.person-img img {
    width: 100%;
    height: auto;
    border-radius: 50%;
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.3);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
}

.icon-button {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
}

.icon-button img {
    width: 50px;
    height: 50px;
}

.person-img:hover .overlay {
    opacity: 1;
}

.linkedin-icon {
    width: 40px;
    height: 40px;
}

.person-info {
    position: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.person-info h3 {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #07334b;
    margin-left: 10px;
}

.person-info p {
    text-align: center;
    font-size: 16px;
    color: gray;
    margin-left: 10px;
}
</style>