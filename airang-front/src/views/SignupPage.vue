<template>
	<section class="signup-wrap">
		<div class="signup-grass grass-1"></div>
		<div class="signup-grass grass-2"></div>
		<div class="signup-grass grass-3"></div>
		<form class="signup-form" @submit.prevent="submitForm">
			<div class="signup-box">
				<label class="signup-label" for="email">이메일</label>
				<input id="email" class="signup-item" type="email" v-model="email" />
			</div>
			<div class="signup-box">
				<label class="signup-label" for="password1">비밀번호</label>
				<input
					id="password1"
					class="signup-item"
					type="password"
					v-model="password1"
				/>
			</div>
			<div class="signup-box">
				<label class="signup-label" for="password2">비밀번호 확인</label>
				<input
					id="password2"
					class="signup-item"
					type="password"
					v-model="password2"
				/>
			</div>
			<button class="signup-btn" type="submit">회원가입</button>
		</form>
	</section>
</template>

<script>
import { mapActions } from 'vuex';
export default {
	data() {
		return {
			email: '',
			password1: '',
			password2: '',
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
				this.$router.push('/');

			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss">
.signup-wrap {
	position: relative;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	.signup-grass {
		width: 25px;
		height: 100px;
		position: absolute;
		top: 50px;
		left: 50%;
		border-top-left-radius: 1rem;
		border-top-right-radius: 1rem;
		border-bottom-left-radius: 1rem;
		border-bottom-right-radius: 1rem;
		background-color: #2f9e44;
		transform: translateX(-50%);
	}
	.grass-1 {
		transform: rotate(-45deg);
		z-index: 1;
	}
	.grass-2 {
		transform: rotate(45deg);
		z-index: 1;
	}
	.grass-3 {
		transform: rotate(0deg);
		z-index: 1;
	}
	.signup-form {
		position: absolute;
		top: 100px;
		left: 50%;
		transform: translateX(-50%);
		width: 550px;
		height: 550px;
		background: #ff922b;
		border-top-left-radius: 15%;
		border-top-right-radius: 15%;
		border-bottom-left-radius: 55%;
		border-bottom-right-radius: 55%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		z-index: 2;

		.signup-box {
			position: relative;
			width: 100%;
			display: flex;
			flex-direction: column;
			align-items: center;
		}
		.signup-label {
			position: absolute;
			top: -24px;
			left: 5rem;
			color: white;
		}
		.signup-item {
			width: 100%;
			max-width: 400px;
			height: 2.5rem;
			padding: 1rem 2rem 1rem;
			font-size: 1rem;
			border: 1px solid black;
			border-top-left-radius: 3rem;
			border-bottom-left-radius: 3rem;
			border-top-right-radius: 3rem;
			border-bottom-right-radius: 3rem;
			border: none;
			outline: none;
			margin-bottom: 2rem;
		}
		.signup-btn {
			display: flex;
			justify-content: center;
			align-items: center;
			width: 100%;
			max-width: 400px;
			height: 2.5rem;
			padding: 1rem;
			border-top-left-radius: 1rem;
			border-bottom-left-radius: 1rem;
			border-top-right-radius: 1rem;
			border-bottom-right-radius: 1rem;
			outline: none;
			border: none;
			cursor: pointer;
			font-size: 1rem;
			font-weight: bold;
			color: white;
			background-color: #2f9e44;
		}
	}
}
</style>
