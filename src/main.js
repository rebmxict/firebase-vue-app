import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import firebase from 'firebase/app'

Vue.prototype.$axios = axios;
Vue.config.productionTip = false

// Your web app's Firebase configuration
const firebaseConfig = {
	apiKey: "AIzaSyDBF80Z_ceLDpXKrieIQyg-5ooHIWtdyyY",
	authDomain: "test-d664d.firebaseapp.com",
	databaseURL: "https://test-d664d.firebaseio.com",
	projectId: "test-d664d",
	storageBucket: "test-d664d.appspot.com",
	messagingSenderId: "157309698492",
	appId: "1:157309698492:web:3fcabdad78cf7ffa53abb9"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let app;

firebase.auth().onAuthStateChanged(user => {
	console.log(user)
	if (!app) {
		app = new Vue({
			router,
			store,
			render: h => h(App)
		}).$mount('#app')
	}
})
