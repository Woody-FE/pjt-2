<template>
	<section>
		<div class="main-wrap">
			<div class="main-board">
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang1.png"
							class="arang alone"
							alt="아랑이1"
						/>
					</div>
					<div class="main-description">
						<p>내가 주인공?!</p>
					</div>
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang2.png"
							class="arang"
							alt="아랑이2"
						/>
					</div>
					<div class="main-description">
						<p>선택가능</p>
					</div>
				</div>
				<div class="main">
					<div class="main-img">
						<img
							src="@/assets/images/character/nukkied_arang3.png"
							class="arang"
							alt="아랑이3"
						/>
					</div>
					<div class="main-description">
						<p>멀티 엔딩</p>
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
	.main-board {
		width: 85%;
		height: 80%;
		padding: 100px 30px;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-wrap: wrap;
		box-shadow: 3px 3px 10px rgba(27, 27, 27, 0.3);
		transform-style: preserve-3d;
		transform: rotateX(65deg);
		.main-img {
			transform-style: preserve-3d;
			.arang {
				width: 250px;
				transform-style: preserve-3d;
				transform: translateY(-150px) rotateX(-85deg);
				box-shadow: 3px 3px 10px rgba(27, 27, 27, 0.3);
			}
			.alone {
				width: 100px;
			}
		}
		.main-description {
			margin-top: 10px;
			text-align: center;
		}
	}
}
</style>
