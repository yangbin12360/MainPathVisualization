import Vue from 'vue'
import Router from 'vue-router'
import graph from '@/components/graph'
import layout from '@/components/layout'
import infoList from '@/components/infoList'

Vue.use(Router)

export default new Router({
    routes: [{
        path: '/',
        name: 'layout',
        component: layout
    }, {
        path: '/graph',
        name: 'graph',
        component: graph
    }, {
        path: '/infoList',
        name: 'infoList',
        component: infoList
    }, ]
})