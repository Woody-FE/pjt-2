<template>
	<section class="signup-wrap">
		<div class="signup-grass grass-1"></div>
		<div class="signup-grass grass-2"></div>
		<div class="signup-grass grass-3"></div>
		<form class="signup-form" @submit.prevent="submitForm">
			<img
				class="signup-logo"
				src="@/assets/images/accounts/signin.png"
				alt="signuplogo"
			/>
			<div class="signup-box">
				<label class="signup-label" for="text">아이 이름</label>
				<input
					id="username"
					class="signup-item"
					type="text"
					v-model="username"
				/>
			</div>
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
		<img
			class="login-arang"
			src="@/assets/images/login/eating3.gif"
			alt="arang"
		/>
		<img
			class="login-ground"
			src="@/assets/images/login/ground.png"
			alt="ground"
		/>
		<img
			class="login-cloud3"
			src="@/assets/images/login/cloud3.png"
			alt="cloud3"
		/>
		<img
			class="login-cloud4"
			src="@/assets/images/login/cloud4.png"
			alt="cloud4"
		/>
		<img
			class="login-items login-grass1"
			src="@/assets/images/login/grass1.png"
			alt="grass1"
		/>
		<img
			class="login-items login-grass2"
			src="@/assets/images/login/grass2.png"
			alt="grass2"
		/>
		<img
			class="login-items login-carrot1"
			src="@/assets/images/login/carrot1.png"
			alt="carrot1"
		/>
		<img
			class="login-items login-carrot2"
			src="@/assets/images/login/carrot2.png"
			alt="carrot2"
		/>
	</section>
</template>

<script>
import { mapActions } from 'vuex';
import { validatePassword, validationName } from '@/utils/validation';

export default {
	data() {
		return {
			email: '',
			password1: '',
			password2: '',
			username: '',
		};
	},
	methods: {
		...mapActions(['SIGNUP']),
		async submitForm() {
			try {
				if (!this.isVaildateName) {
					alert('※ 이름은 공백제외 2~5자 한글입니다.');
					return;
				}
				if (!this.isValidatePassword1) {
					alert('※ 비밀번호는 공백제외 8자 이상 15자 이하입니다.');
					return;
				}
				if (!this.isEqualPassword) {
					alert('※ 비밀번호를 한번 더 확인해주세요!');
					return;
				}
				const userInfo = {
					username: this.username,
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
	computed: {
		isVaildateName() {
			const name = this.username;
			if (name.length === 0) {
				return false;
			}
			return validationName(name);
		},
		isValidatePassword1() {
			const password = this.password1;
			if (!password) {
				return true;
			}
			return validatePassword(password);
		},
		isEqualPassword() {
			const password1 = this.password1;
			const password2 = this.password2;
			if (!password1 && !password2) {
				return true;
			}
			return password1 === password2;
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
		top: 25px;
		left: 50%;
		border-top-left-radius: 1rem;
		border-top-right-radius: 1rem;
		border-bottom-left-radius: 1rem;
		border-bottom-right-radius: 1rem;
		background-color: #2f9e44;
		transform: translateX(-50%);
	}
	@-webkit-keyframes grass-1 {
		0% {
			transform: rotate(-60deg);
		}
		50% {
			transform: rotate(-45deg);
		}
		100% {
			transform: rotate(-60deg);
		}
	}
	@-webkit-keyframes grass-2 {
		0% {
			transform: rotate(60deg);
		}
		50% {
			transform: rotate(45deg);
		}
		100% {
			transform: rotate(60deg);
		}
	}
	.grass-1 {
		transform: rotate(-45deg);
		z-index: 1;
		animation: grass-1 1s infinite alternate;
		animation-timing-function: 2s;
	}
	.grass-2 {
		transform: rotate(45deg);
		z-index: 1;
		animation: grass-2 1s infinite alternate;
		animation-timing-function: 2s;
	}
	.grass-3 {
		transform: rotate(0deg);
		z-index: 1;
	}
	.signup-form {
		position: absolute;
		top: 70px;
		left: 50%;
		transform: translateX(-50%);
		width: 550px;
		height: 520px;
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
		.signup-logo {
			position: absolute;
			top: 5%;
			left: 60%;
			z-index: 999;
			width: 150px;
		}
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
			max-width: 368px;
			height: 2rem;
			padding: 0.25rem 1rem;
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
	.login-arang {
		width: 10%;
		position: absolute;
		bottom: -505px;
		right: 6%;
	}
	.login-cloud3 {
		width: 17%;
		position: absolute;
		top: 12%;
		left: 3%;
	}
	.login-cloud4 {
		width: 12%;
		position: absolute;
		top: 5%;
		left: 14%;
	}
	.login-ground {
		width: 100%;
		height: 130px;
		position: absolute;
		bottom: -610px;
	}
	.login-items {
		width: 6%;
		position: absolute;
	}
	.login-grass1 {
		bottom: -515px;
		right: 19%;
	}
	.login-grass2 {
		width: 3%;
		bottom: -520px;
		right: 18%;
	}
	.login-carrot1 {
		bottom: -580px;
		left: 15%;
	}
	.login-carrot2 {
		bottom: -550px;
		left: 11%;
	}
}
</style>
