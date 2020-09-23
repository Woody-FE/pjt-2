<template>
	<section>
		<div class="main-wrap">
			<div class="main-board">
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang1.png"
							class="arang arang1"
							alt="아랑이1"
						/>
					</div>
					<div class="main-description">
						<p class="arang1">내가 주인공?!</p>
					</div>
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang2.png"
							class="arang arang2"
							alt="아랑이2"
						/>
					</div>
					<div class="main-description">
						<p class="arang2">선택가능</p>
					</div>
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang3.png"
							class="arang arang3"
							alt="아랑이3"
						/>
					</div>
					<div class="main-description">
						<p class="arang3">멀티 엔딩</p>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
export default {};
</script>

<style lang="scss">
.main-wrap {
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-wrap: wrap;
	margin-top: 100px;
	perspective: 1000px;
	@media screen and (max-width: 1024px) {
		perspective: 900px;
	}
	@media screen and (max-width: 768px) {
		perspective: 1100px;
	}
	.main-board {
		width: 60vw;
		height: 55vh;
		display: flex;
		justify-content: center;
		align-items: center;
		box-shadow: 3px 3px 10px rgba(27, 27, 27, 0.3);
		transform-style: preserve-3d;
		transform: rotateX(65deg);
		.main-img {
			transform-style: preserve-3d;
			.arang {
				width: 250px;
				transform-style: preserve-3d;
				box-shadow: 3px 0 10px rgba(27, 27, 27, 0.3);
				@media screen and (max-width: 1024px) {
					width: 220px;
				}
				@media screen and (max-width: 768px) {
					width: 170px;
				}
			}
			.arang1 {
				width: 100px;
				transform: translateY(-220px) rotateX(-85deg);
				@media screen and (max-width: 1024px) {
					width: 90px;
				}
				@media screen and (max-width: 768px) {
					width: 70px;
					transform: translateY(-20px) rotateX(-85deg);
				}
			}
			.arang2 {
				transform: translateY(-50px) rotateX(-85deg);
				@media screen and (max-width: 768px) {
					transform: translateY(130px) rotateX(-85deg);
				}
			}
			.arang3 {
				transform: translateY(-400px) rotateX(-85deg);
				@media screen and (max-width: 768px) {
					transform: translateY(-320px) rotateX(-85deg);
				}
			}
		}
		.main-description {
			margin-top: 10px;
			transform-style: preserve-3d;
			p {
				transform-style: preserve-3d;
				transform: rotateX(-85deg);
			}
		}
	}
}
</style>
