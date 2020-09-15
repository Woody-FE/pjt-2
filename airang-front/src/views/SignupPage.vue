<template>
	<section class="signup-wrap">
		<form class="signup-form" @submit.prevent="submitForm">
			<input class="signup-item" type="email" v-model="email" />
			<input class="signup-item" type="password" v-model="password1" />
			<input class="signup-item" type="password" v-model="password2" />
			<button class="signup-btn" type="submit">로그인</button>
		</form>
	</section>
</template>

<script>
import { mapActions } from 'vuex';
export default {
	data() {
		return {
			email: '',
			password: '',
		};
	},
	methods: {
		...mapActions(['SIGNUP']),
		async submitForm() {
			try {
				const userInfo = {
					email: this.email,
					password1: this.password1,
					password2: this.password2,
				};
				await this.SIGNUP(userInfo);
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss"></style>
