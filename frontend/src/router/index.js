import { createRouter, createWebHashHistory } from "vue-router";
import WebHome from "../views/WebHome.vue";
import WebAbout from "../views/WebAbout.vue";
import WebContact from "../views/WebContact.vue";
import ImgProc from "../views/ImgProc.vue";
import EmailSender from "../views/EmailSender.vue";
import EmailTemp from "@/views/EmailTemp.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: WebHome
    },
    {
        path: "/about",
        name: "About",
        component: WebAbout
    },
    {
        path: "/contact",
        name: "Contact",
        component: WebContact
    },
    {
        path: "/img_proc",
        name: "ImgProc",
        component: ImgProc
    },
    {
        path: "/email_temp",
        name: "EmailTemp",
        component: EmailTemp
    },
    {
        path: "/email_sender",
        name: "EmailSender",
        component: EmailSender
    },
]
const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router;