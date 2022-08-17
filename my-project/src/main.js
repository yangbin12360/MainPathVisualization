// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/*import vuex*/
import { store } from './store/store'

import axios from 'axios'

// 导入element组件
import ElementUI from 'element-ui'; //引入ElementUI组件库
import 'element-ui/lib/theme-chalk/index.css'; //引入ElementUI全部样式


Vue.use(ElementUI); //使用插件

Vue.prototype.$axios = axios
    /* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store: store,
    components: { App },
    template: '<App/>'
})