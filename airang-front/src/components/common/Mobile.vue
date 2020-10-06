<template>
	<section class="mobile">
		<div class="text-wrap">
			<p>태블릿 보다</p>
			<p>같거나 큰 화면으로</p>
			<p>접속해주세요</p>
			<em>( 768px 이상 )</em>
			<img src="@/assets/images/character/nukkied_arang1.png" alt="" />
		</div>
	</section>
</template>

<script>
export default {
	name: 'Mobile',
};
</script>

<style lang="scss">
.mobile {
	display: block;
	width: 100vw;
	height: 100vh;
	.text-wrap {
		display: flex;
		height: 100%;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		font-size: 2rem;
		p {
			margin: 1rem 0 1rem 0;
		}
		em {
			margin: 1rem 0 1rem 0;
			color: $carrotGreen;
		}
		img {
			width: 150px;
		}
	}
}
@media screen and (min-width: 768px) {
	.mobile {
		display: none;
	}
}
</style>
