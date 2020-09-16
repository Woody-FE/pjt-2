<template>
	<section class="profileInfo-wrap">
		<img
			class="profileInfo-img"
			src="@/assets/images/demo_profile.gif"
			alt="profileImg"
		/>
		<p class="profileInfo-name">황영준</p>
		<section class="btn-box">
			<router-link to="/profile/1/modifyinfo">
				<button class="btn-update__img btn">정보수정</button>
			</router-link>
			<button class="btn-update__info btn">사진수정</button>
		</section>
	</section>
</template>

<script>
export default {
	data() {
		return {
			userData: {
				name: null,
				imgPath: null,
			},
		};
	},
	methods: {},
};
</script>

<style lang="scss" scoped>
.profileInfo-wrap {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	.profileInfo-img {
		width: 15rem;
		height: 15rem;
		margin-top: 2rem;
		margin-bottom: 1rem;
		border-radius: 50%;
		border: 1px solid yellow;
	}
	.profileInfo-name {
		font-size: 3rem;
		margin-bottom: 1.5rem;
	}
	.btn-box {
		display: flex;
		margin-bottom: 3rem;
		.btn {
			width: 100px;
			height: 40px;
			color: white;
			font-size: 1rem;
			background: $lightGreen;
			border-radius: 15px;
			border: none;
			&:hover {
				cursor: pointer;
				background: $green;
			}
		}
		.btn-update__img {
			margin-right: 0.5rem;
		}
		.btn-update__info {
			margin-right: 0rem;
		}
	}
}
</style>
