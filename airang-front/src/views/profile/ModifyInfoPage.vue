<template>
	<section class="modify-wrap">
		<div class="input-box">
			<span>
				<img
					class="decoration"
					src="@/assets/images/background/sp.png"
					alt="sprout"
				/>이메일
			</span>
			<input
				class="input-form email-input__form"
				type="text"
				v-model="userData.email"
				readonly
			/>
		</div>
		<div class="input-box">
			<span class="">
				<img
					class="decoration"
					src="@/assets/images/background/sp.png"
					alt="sprout"
				/>이름
			</span>
			<input class="input-form" type="text" v-model="userData.username" />
			<button class="name-btn" @click="changeName">ㄷㅈ</button>
		</div>
		<div class="input-box">
			<span class="">
				<img
					class="decoration"
					src="@/assets/images/background/sp.png"
					alt="sprout"
				/>비밀번호
			</span>
			<input
				class="input-form"
				type="text"
				v-model="userPassword.new_password1"
			/>
		</div>
		<div class="input-box">
			<span class="">
				<img
					class="decoration"
					src="@/assets/images/background/sp.png"
					alt="sprout"
				/>비밀번호 확인
			</span>
			<input
				class="input-form"
				type="text"
				v-model="userPassword.new_password2"
			/>
		</div>
		<section class="btn-box">
			<router-link to="/profile/1">
				<button class="btn btn-cancle">취소</button>
			</router-link>
			<button class="btn btn-update" @click="patchData">수정</button>
		</section>
		<footer class="modify-footer"></footer>
	</section>
</template>

<script>
import { getUserProfile, patchUserName, changePassword } from '@/api/profile';
// import cookies from 'vue-cookies';
// import { mapMutations } from 'vuex';

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
		// ...mapMutations(['setId']),
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
				const temp = await patchUserName(id, content);
				console.log(temp);
			} catch (error) {
				console.log(error);
			}
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
		margin-bottom: 2rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		span {
			font-size: 1rem;
			position: relative;
			margin-right: 35%;
		}
		.decoration {
			position: absolute;
			top: -7px;
			left: 0;
			width: 15px;
		}
		.input-form {
			margin-top: 8px;
			width: 50%;
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
	}
	.btn-box {
		display: flex;
		justify-content: center;
		margin-bottom: 3rem;
		.btn {
			width: 100px;
			height: 40px;
			font-size: 1rem;
			border-radius: 15px;
			border: none;
			&:hover {
				cursor: pointer;
				background: $green;
			}
		}
		.btn-cancle {
			background: white;
			margin-right: 0.5rem;
			border: $lightGreen;
		}
		.btn-update {
			color: white;
			background: $lightGreen;
			margin-right: 0rem;
		}
	}
	.modify-footer {
		height: 50px;
	}
}
</style>
