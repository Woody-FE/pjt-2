<template>
	<section class="login-wrap">
		<div class="login-grass grass-1"></div>
		<div class="login-grass grass-2"></div>
		<div class="login-grass grass-3"></div>
		<form class="login-form" @submit.prevent="submitForm">
			<img
				class="login-logo"
				src="@/assets/images/accounts/login.png"
				alt="loginlogo"
			/>
			<div class="login-brown-1"></div>
			<div class="login-brown-2"></div>
			<div class="login-brown-3"></div>
			<div class="login-box">
				<label class="login-label" for="email">이메일</label>
				<input id="email" class="login-item" type="email" v-model="email" />
			</div>
			<div class="login-box">
				<label class="login-label" for="password">패스워드</label>
				<input
					id="password"
					class="login-item"
					type="password"
					v-model="password"
				/>
			</div>
			<button class="login-btn" type="submit" :disabled="disabledBtn">
				로그인
			</button>
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
import { loginUser } from '@/api/auth';
import bus from '@/utils/bus';

export default {
	data() {
		return {
			email: '',
			password: '',
		};
	},
	methods: {
		...mapActions(['LOGIN']),
		async submitForm() {
			try {
				const userInfo = { email: this.email, password: this.password };
				const { data } = await loginUser(userInfo);
				this.$store.dispatch('SETUP_USER', data);
				if (this.$route.query.guide) {
					this.$router.push('/bookshelf');
				} else {
					this.$router.push('/');
				}
			} catch (error) {
				bus.$emit('show:warning', '이메일, 비밀번호를 확인해주세요!');
			}
		},
	},
	computed: {
		disabledBtn() {
			return !this.email || !this.password;
		},
	},
};
</script>

<style lang="scss">
.login-wrap {
	position: relative;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	.login-grass {
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
		animation: grass-1 2s infinite alternate;
		animation-timing-function: 2s;
	}
	.grass-2 {
		transform: rotate(45deg);
		z-index: 1;
		animation: grass-2 2s infinite alternate;
		animation-timing-function: 2s;
	}
	.grass-3 {
		transform: rotate(0deg);
		z-index: 1;
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
	.login-form {
		position: absolute;
		top: 100px;
		left: 50%;
		transform: translateX(-50%);
		width: 500px;
		height: 470px;
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
		.login-logo {
			position: absolute;
			top: 6%;
			left: 65%;
			z-index: 999;
			width: 110px;
		}
		.login-brown-1 {
			position: absolute;
			background: brown;
			border-radius: 4px;
			width: 60px;
			height: 2px;
			top: 50px;
			left: 15%;
		}
		.login-brown-2 {
			position: absolute;
			background: brown;
			border-radius: 4px;
			width: 90px;
			height: 2px;
			top: 80px;
			left: 17%;
		}
		.login-brown-3 {
			position: absolute;
			background: brown;
			border-radius: 4px;
			transform: translateX(-50%);
			width: 30px;
			height: 2px;
			top: 400px;
			left: 70%;
		}
		.login-box {
			position: relative;
			width: 60%;
			display: flex;
			flex-direction: column;
			align-items: center;
		}
		.login-label {
			position: absolute;
			top: -1.3rem;
			left: 1rem;
			color: white;
		}
		.login-item {
			width: 90%;
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
		.login-btn {
			display: flex;
			justify-content: center;
			align-items: center;
			width: 60%;
			max-width: 400px;
			height: 2.5rem;
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
			&:disabled {
				cursor: default;
				opacity: 0.7;
			}
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
