import Vue from "vue";
import Vuex from "vuex"

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        id: "null",
        title: "null",
        abstract: "null",
        applicant: "null",
        time: "null",
        CPC: "null",
        IPC: "null",
        citeNum: "null",
        beCiteNum: "null"
    }
});