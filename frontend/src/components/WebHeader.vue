<!--src/components/WebHeader.vue-->

<template>
    <header class="topbar">
        <div class="topbar-content">
            <div class="topbar-left">
                <router-link to="/" role="button" class="topbar-button">Tool-Box</router-link>
                <img :src="logo" width="60px" height="60px" style="margin: 15px 20px;" alt="logo">
            </div>
            <nav class="menu">
                <router-link to="/" role="button" class="topbar-menu-button">Home</router-link>
                <div class="dropdown">
                    <a class="dropbtn">Services</a>
                    <div class="dropdown-content">
                        <router-link to="/img_proc">Image Processor</router-link>
                        <router-link to="/email_sender">Auto Email Sender</router-link>
                    </div>
                </div>
                <router-link to="/about" role="button" class="topbar-menu-button">About</router-link>
                <router-link to="/contact" role="button" class="topbar-menu-button">Contact</router-link>
            </nav>
        </div>
    </header>
</template>

<script>
import logo from '@/assets/images/deep-learning.png';
export default {
    name: 'WebHeader',
    data() {
        return {
            logo
        };
    },
};
</script>

<style>
.topbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #f1f1f1;
    z-index: 1000;
}

.topbar-button {
    text-decoration: none;
    text-align: left;
    margin-right: 20px;
    font-weight: bold;
    font-size: 30px;
    color: #07334b;
    margin-top: 30px;
}

.topbar-content {
    display: flex;
    margin-left: 150px;
    margin-right: 150px;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0;
}

.topbar-left {
    display: flex;
}

.menu {
    display: flex;
    align-items: center;
    margin-left: auto;
}

.topbar-menu-button {
    text-decoration: none;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 20px;
    text-align: center;
    color: #07334b;
    background-color: #f1f1f1;
    transition: background-color 0.3s;
}

.menu>.dropdown {
    padding: 10px 20px;
    font-weight: bold;
    font-size: 20px;
    text-align: center;
    color: #07334b;
    background-color: #f1f1f1;
    transition: background-color 0.3s;
}

.topbar-menu-button:hover,
.menu>.dropdown:hover {
    background-color: #e0e0e0;
}

.dropbtn {
    font-size: 20px;
    color: #07334b;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: 0.4s;
}

.dropbtn:hover {
    opacity: 0.7;
}

.dropdown {
    position: relative;
}

.dropndown a {
    text-align: center;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 120px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
    text-align: center;
}

/* Links inside the dropdown */
.dropdown-content a {
    color: #07334b;
    padding: 12px 12px;
    text-decoration: none;
    display: block;
    text-align: left;
    font-size: 16px;
    font-weight: lighter;
    line-height: 1.5;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
    background-color: #f1f1f1;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content,
.dropdown-content:hover {
    display: block;
}
</style>