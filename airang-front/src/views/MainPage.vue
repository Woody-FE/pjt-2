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
						<span class="arang1-shadow"></span>
					</div>
					<div class="main-description">
						<p class="sign1">
							<span class="sign">내가 주인공?!</span>
							<span class="stick stick1"></span>
						</p>
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
						<p class="sign2">
							<span class="sign">선택가능</span>
							<span class="stick"></span>
						</p>
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
						<p class="sign3">
							<span class="sign">멀티 엔딩</span>
							<span class="stick"></span>
						</p>
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
				box-shadow: -3.5px 15px 5px rgba(27, 27, 27, 0.3);
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
			.arang1-shadow {
				position: absolute;
				top: 100px;
				right: -70px;
				padding: 40px;
				border-radius: 50%;
				background: rgba(189, 92, 24, 0.3);
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
				position: relative;
				transform-style: preserve-3d;
				.sign {
					padding: 5px 12px;
					font-size: 12px;
					background: #2f9e44;
					border-radius: 40px 10px 30px;
				}
				.stick {
					padding: 5px 3px;
					background: #2f9e44;
					position: absolute;
					top: 20px;
					right: 225px;
					border-radius: 4px;
				}
				.stick1 {
					right: 55px;
				}
			}
			.sign1 {
				transform: translateY(-100px) rotateX(-55deg);
			}
			.sign2 {
				transform: translateY(0px) rotateX(-70deg);
			}
			.sign3 {
				transform: translate(-50px, -250px) rotateX(-85deg) rotateY(-15deg);
			}
		}
	}
}
</style>
