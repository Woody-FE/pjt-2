<template>
	<section class="modify-wrap">
		<div class="input-box">
			<span>
				<img
					class="decoration"
					src="@/assets/images/character/sp.png"
					alt="sprout"
				/>이메일
			</span>
			<input
				class="input-form email-input__form"
				type="text"
				v-model="userData.email"
				readonly
			/>
			<div class="msg-box"></div>
		</div>
		<div class="input-box">
			<span class="">
				<img
					class="decoration"
					src="@/assets/images/character/sp.png"
					alt="sprout"
				/>이름
			</span>
			<input class="input-form" type="text" v-model="userData.username" />
			<div class="msg-box">
				<p v-if="!isVaildateName" class="hidden-msg1 msg">
					※ 이름은 공백제외 2~5자 한글입니다.
				</p>
			</div>
		</div>
		<div class="input-box">
			<span class="">
				<img
					class="decoration"
					src="@/assets/images/character/sp.png"
					alt="sprout"
				/>비밀번호
			</span>
			<input
				class="input-form"
				type="password"
				v-model="userPassword.new_password1"
			/>
			<div class="msg-box">
				<p v-if="!isValidatePassword1" class="hidden-msg1 msg">
					※ 비밀번호는 공백제외 8자 이상 15자 이하입니다.
				</p>
			</div>
		</div>

		<div class="input-box">
			<span class="">
				<img
					class="decoration"
					src="@/assets/images/character/sp.png"
					alt="sprout"
				/>비밀번호 확인
			</span>
			<input
				class="input-form"
				type="password"
				v-model="userPassword.new_password2"
			/>
			<div class="msg-box">
				<p v-if="!isEqualPassword" class="hidden-msg2 msg">
					※ 비밀번호를 한번 더 확인해주세요!
				</p>
			</div>
		</div>

		<section class="btn-box">
			<router-link to="/profile/">
				<button class="btn btn-cancle">취소</button>
			</router-link>
			<button
				:disabled="!isValidatePassword1 || !isEqualPassword"
				class="btn btn-update"
				@click="patchData"
			>
				비밀번호수정
			</button>
			<button
				:disabled="!isVaildateName"
				class="name-btn btn"
				@click="changeName"
			>
				이름수정
			</button>
		</section>
		<footer class="modify-footer"></footer>
	</section>
</template>

<script>
import { getUserProfile, patchUserName, changePassword } from '@/api/profile';
import { validatePassword, validationName } from '@/utils/validation';

export default {
	data() {
		return {
			userData: {
				email: null,
				username: null,
				password: null,
			},
			userPassword: {
				new_password1: null,
				new_password2: null,
			},
		};
	},
	methods: {
		async fetchData() {
			try {
				const id = this.$store.getters.getId;
				const { data } = await getUserProfile(id);
				this.userData.email = data.email;
				this.userData.username = data.username;
			} catch (error) {
				console.log(error);
			}
		},
		async patchData() {
			try {
				const content = this.userPassword;
				await changePassword(content);
				this.$router.push('/profile/');
			} catch (error) {
				console.log(error);
			}
		},
		async changeName() {
			try {
				const content = {
					username: this.userData.username,
				};
				const id = this.$store.getters.getId;
				await patchUserName(id, content);
				this.$router.push('/profile/');
			} catch (error) {
				console.log(error);
			}
		},
	},
	computed: {
		isVaildateName() {
			const name = this.userData.username;
			if (name.length === 0) {
				return false;
			}
			return validationName(name);
		},
		isValidatePassword1() {
			const password = this.userPassword.new_password1;
			if (!password) {
				return true;
			}
			return validatePassword(password);
		},
		isEqualPassword() {
			const password1 = this.userPassword.new_password1;
			const password2 = this.userPassword.new_password2;
			if (!password1 && !password2) {
				return true;
			}
			return password1 == password2;
		},
	},
	created() {
		this.fetchData();
	},
};
</script>

<style lang="scss" scoped>
.modify-wrap {
	padding-left: 7rem;
	padding-right: 7rem;
	margin-top: 4rem;
	.input-box {
		display: flex;
		flex-direction: column;
		align-items: center;
		span {
			font-size: 1rem;
			position: relative;
			margin-right: 50%;
		}
		.decoration {
			position: absolute;
			top: -7px;
			left: 0;
			width: 15px;
		}
		.input-form {
			margin-top: 8px;
			width: 70%;
			height: 3rem;
			padding-left: 1rem;
			padding-right: 1rem;
			border-radius: 1rem;
			border: none;
			font-size: 1rem;
		}
		.email-input__form {
			background: rgb(199, 199, 199);
		}
		.msg-box {
			width: 100%;
			height: 2rem;
			text-align: center;
		}
	}
	.btn {
		height: 40px;
		font-size: 1rem;
		border-radius: 15px;
		border: none;
	}
	.name-btn {
		color: white;
		background: $carrotGreen;
		&:hover {
			cursor: pointer;
			background: $green;
		}
	}
	.btn-box {
		display: flex;
		justify-content: center;
		margin-bottom: 3rem;

		.btn-cancle {
			background: white;
			margin-right: 0.5rem;
			border: $lightGreen;
			color: black;
			&:hover {
				cursor: pointer;
				background: $green;
			}
		}
		.btn-update {
			color: white;
			background: $carrotGreen;
			margin-right: 0.5rem;
			&:hover {
				cursor: pointer;
				background: $green;
			}
		}
	}
	.modify-footer {
		height: 50px;
	}
}
.msg {
	color: crimson;
	font-size: 0.9rem;
	font-weight: 100;
}
</style>
