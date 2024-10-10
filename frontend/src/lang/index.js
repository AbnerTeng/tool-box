import Vue from 'vue'
import Cookies from 'js-cookie'
import VueI18n from 'vue-i18n'
import twLocale from './zh_tw'
import enLocale from './en'
import locale_TW from 'element-ui/lib/locale/lang/zh-TW'
import locale_EN from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale'

Vue.use(VueI18n)
locale.i18n((key, value) => i18n.t(key, value))

const messages = {
    en: {
        ...enLocale,
        ...locale_EN
    },
    zh_tw: {
        ...twLocale,
        ...locale_TW
    },
}

const languageKey = 'language'
const chooseLanguage = Cookies.get('language')

export const getLanguage = () => {
    Cookies.get(languageKey)
    if (chooseLanguage) { return chooseLanguage }

    const language = (navigator.language).toLowerCase()
    const locales = Object.keys(messages) // { en, zh_tw, jp }
    for (const locale of locales) {
        if (language.indexOf(locale) > -1) {
            return locale
        }
    }
    return 'zh_tw' // 沒選擇語言的時候，預設轉到繁體中文
}


export const setLanguage = (language) => {
    i18n.locale = language
    Cookies.set(languageKey, language)
}

const i18n = new VueI18n({
    locale: getLanguage(),
    messages,
    silentTranslationWarn: true
})

export default i18n