<template>
	<div>
		Logged in
		<span v-if='loggedIn'>Yes</span>
		<span v-else>No</span>
		<div>
			<button @click='signOut'>Sign out</button>
		</div>
	</div>
</template>

<script>
	import * as firebase from 'firebase/app'
	import 'firebase/auth'

	export default {
		created() {
			firebase.auth().onAuthStateChanged(user => {
				this.loggedIn = !!user;
				// if (user) {
				// 	this.loggedIn = true
				// } else {
				// 	this.loggedIn = false
				// }
			})
		},
		methods: {
			async signOut() {
				try {
					const data = await firebase.auth().signOut()
					this.$router.replace({name: 'login'})
					console.log(data)
				} catch(err) {
					console.log(err)
				}
			}
		},
		data() {
			return {
				loggedIn: false
			}
		}
	}
</script>

<style lang="scss" scoped>
	
</style>