<template>
	<div>
		Login
		<form @submit.prevent='pressed'>
			<div class='login'>
				<input type="email" placeholder="login" v-model='email'>
			</div>
			<div class='password'>
				<input type="password" placeholder="password" v-model='password'>
			</div>
			<button type='submit'>Login</button>
		</form>
		<div class='error' v-if='error'>{{error.message}}</div>
		<span>Need an account? Click here to <router-link to='/register'>Register</router-link></span>
	</div>
</template>

<script>
	import * as firebase from 'firebase/app';
	import 'firebase/auth';

	export default {
		methods: {
			async pressed() {
				try {
					const val = await firebase.auth().signInWithEmailAndPassword(this.email, this.password)
					this.$router.replace({name: 'secret'})
					console.log(val)
				} catch(err) {
					console.log(err)
				}
			}
		},
		data() {
			return {
				email: '',
				password: '',
				error: ''
			}
		}
	}
</script>

<style lang="scss" scoped>
input {
	width: 400px;
	padding: 30px;
	margin: 20px;
	font-size: 21px;
}

button {
	width: 400px;
	height: 75px;
	font-size: 100%;
}

.error {
	color: red;
}
</style>