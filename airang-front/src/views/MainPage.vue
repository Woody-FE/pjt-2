<template>
	<section>
		<div class="main-wrap">
			<div class="main-board">
				<div class="wheel">
					<BigWheel />
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang1.png"
							class="arang arang1"
							alt="아랑이1"
						/>
						<span class="arang-shadow arang1-shadow"></span>
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
						<span class="arang-shadow arang2-shadow"></span>
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
						<span class="arang-shadow arang3-shadow"></span>
					</div>
					<div class="main-description">
						<p class="sign3">
							<span class="sign multi-sign">멀티 엔딩</span>
							<span class="stick"></span>
						</p>
					</div>
				</div>
				<router-link class="start-btn btn" to="/bookshelf">START</router-link>
			</div>
		</div>
	</section>
</template>

<script>
import BigWheel from '@/components/main/BigWheel.vue';
export default {
	components: {
		BigWheel,
	},
};
</script>

<style lang="scss">
@include common-btn();
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
	.wheel {
		position: absolute;
		top: -400px;
		transform: rotate3d(1, 0, 0, -65deg);
	}
	.main-board {
		width: 60vw;
		height: 55vh;
		margin-top: 80px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		box-shadow: 3px 3px 10px rgba(27, 27, 27, 0.3);
		transform-style: preserve-3d;
		transform: rotateX(65deg);
		.main-img {
			transform-style: preserve-3d;
			.arang {
				width: 250px;
				transform-style: preserve-3d;
				position: relative;
				z-index: 999;
				@media screen and (max-width: 1024px) {
					width: 220px;
				}
				@media screen and (max-width: 768px) {
					width: 170px;
				}
			}
			.arang1 {
				width: 100px;
				transform-style: preserve-3d;
				transform: translateY(-220px) rotateX(-85deg);
				@media screen and (max-width: 1024px) {
					width: 90px;
					margin: 0 10px;
				}
				@media screen and (max-width: 768px) {
					width: 70px;
					margin: 0 20px;
					transform: translateY(-150px) rotateX(-85deg);
				}
			}
			.arang2 {
				transform: translateY(-50px) rotateX(-85deg);
			}
			.arang3 {
				transform: translateY(-200px) rotateX(-85deg);
				@media screen and (max-width: 768px) {
					transform: translate(-30px, -210px) rotateX(-85deg);
				}
			}
			.arang-shadow {
				position: absolute;
				border-radius: 50%;
				background: rgba(189, 92, 24, 0.3);
				box-shadow: 0 0 15px rgba(189, 92, 24, 0.5);
			}
			.arang1-shadow {
				top: 110px;
				right: -62px;
				padding: 20px 30px;
				@media screen and (max-width: 1024px) {
					right: -45px;
				}
				@media screen and (max-width: 768px) {
					top: 100px;
					right: -15px;
					padding: 10px 30px;
				}
			}
			.arang2-shadow {
				top: 220px;
				right: 30px;
				padding: 20px 100px;
				@media screen and (max-width: 1024px) {
					top: 200px;
					padding: 20px 80px;
				}
				@media screen and (max-width: 768px) {
					top: 170px;
					right: -10px;
					padding: 20px 100px;
				}
			}
			.arang3-shadow {
				top: 50px;
				right: 10px;
				padding: 30px 150px;
				@media screen and (max-width: 1024px) {
					right: 23px;
					padding: 20px 120px;
				}
				@media screen and (max-width: 768px) {
					top: 10px;
					right: 40px;
					padding: 20px 100px;
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
					background: #77411d;
					border-radius: 40px 10px 30px;
					@media screen and (max-width: 1024px) {
						padding: 4px 9px;
						font-size: 12px;
					}
				}
				.multi-sign {
					padding: 5px 18px;
					font-size: 16px;
				}
				.stick {
					padding: 5px 3px;
					background: #77411d;
					position: absolute;
					top: 20px;
					right: 225px;
					border-radius: 4px;
					@media screen and (max-width: 1024px) {
						right: 200px;
					}
					@media screen and (max-width: 768px) {
						right: 120px;
					}
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
				transform: translate(-60px, -170px) rotateX(-85deg) rotateY(-15deg);
			}
		}
	}
	.start-btn {
		position: absolute;
		bottom: 50px;
		right: 10px;
		padding: 20px 30px;
		font-size: 2rem;
		background-color: $carrotGreen;
		box-shadow: 0 10px $green;
		cursor: pointer;
		transform: rotateX(-5deg);
		&:active {
			background-color: $green;
			box-shadow: 0 3px $green;
			transform: translateY(6px);
		}
	}
}
</style>
