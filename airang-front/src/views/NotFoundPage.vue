<template>
	<section class="notFound-wrap">
		<div class="notFound-field1">
			<img
				class="notFound-img"
				src="@/assets/images/character/nokkied_sick_tokki.png"
				alt="nukkied-girl"
			/>
		</div>
		<div class="notFound-field2">
			<p>여기가 아니야!</p>
			<p></p>
			<p>내가 길을 알려줄께!</p>
			<button class="notFound-btn" @click="goBack">돌아가기</button>
		</div>
	</section>
</template>

<script>
export default {
	methods: {
		goBack() {
			this.$router.push('/');
		},
	},
};
</script>

<style lang="scss" scoped>
.notFound-wrap {
	display: flex;
	margin-top: 5rem;
	.notFound-field1 {
		width: 50%;
		display: flex;
		justify-content: flex-end;
		.notFound-img {
			height: 400px;
		}
	}
	.notFound-field2 {
		width: 50%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: flex-start;
		align-items: center;
		p {
			font-size: 2rem;
		}
		.notFound-btn {
			margin-top: 2rem;
			width: 200px;
			height: 40px;
			font-size: 1rem;
			border-radius: 15px;
			border: none;
			color: white;
			background: $carrotGreen;
			margin-right: 0.5rem;
			&:hover {
				cursor: pointer;
				background: $green;
			}
		}
	}
}
</style>
