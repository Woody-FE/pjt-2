<template>
	<section class="mystory-wrap">
		<div class="mystory-bookcover">
			<section class="mystory-page">
				<div class="mystory-face mystory-cover">
					<!-- 팀 소개책 커버 이미지 -->
					<img
						class="mystory-cover__img"
						src="@/assets/images/default_book.jpg"
						alt=""
					/>
				</div>
				<div class="mystory-face">하이</div>
			</section>
			<section class="mystory-page">
				<div class="mystory-face">하이</div>
			</section>
		</div>
	</section>
</template>

<script>
export default {
	mounted() {
		const cover = document.querySelector('.mystory-cover__img');
		if (cover) {
			cover.addEventListener('load', () => {
				const page = document.querySelectorAll('.mystory-page');
				setTimeout(function() {
					page[0].classList.add('flipped');
				}, 750);
			});
		}
	},
};
</script>

<style lang="scss" scoped>
.mystory-wrap {
	position: relative;
	width: 100%;
	min-height: 100vh;
	.mystory-bookcover {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		width: 90vw;
		height: 95vh;
		transform-style: preserve-3d;
		margin: auto;
		.mystory-page {
			position: absolute;
			left: 50%;
			top: 0;
			box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
			width: 50%;
			height: 100%;
			transform-style: preserve-3d;
			transition: 1s;
			border: 1px solid lightgray;
			.mystory-face {
				position: absolute;
				left: 0;
				box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
				top: 0;
				width: 100%;
				height: 100%;
				background: white;
				color: black;
				backface-visibility: hidden;
			}
			&:nth-child(1) {
				z-index: 3;
				transform-origin: left;
			}
			&:nth-child(2) {
				z-index: 2;
				transform-origin: left;
			}
		}
	}
}
.mystory-face:nth-child(2) {
	transform: rotateY(-180deg);
}
.flipped {
	transform: rotateY(-180deg);
}
.mystory-cover {
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	.mystory-cover__img {
		width: 100%;
		height: 100%;
		object-fit: fill;
	}
}
</style>
