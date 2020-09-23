<template>
	<div class="bb-custom-side">
		<div
			:key="script.id"
			v-for="(script, index) in scripts"
			:class="[count === index ? 'bb-abled' : 'bb-disabled']"
		>
			<div class="portrait-box">
				<img
					class="portrait-img"
					src="@/assets/images/character/arang1.png"
					alt=""
				/>
				<p class="portrait-p">나레이션</p>
			</div>
			<p v-html="script.content"></p>
		</div>
		<div class="text-btn">
			<button class="bb-left-btn" @click="beforePage">
				<i class="icon ion-md-arrow-round-back"></i>
			</button>
			<button class="bb-right-btn" @click="afterPage">
				<i class="icon ion-md-arrow-round-forward"></i>
			</button>
		</div>
	</div>
</template>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script>
export default {
	methods: {
		beforePage() {
			if (this.count <= 0) {
				$('#bb-bookblock').bookblock('prev');
				return;
			}
			this.count--;
		},
		afterPage() {
			if (this.count >= this.scripts.length - 1) {
				$('#bb-bookblock').bookblock('next');
				return;
			}
			this.count++;
		},
	},
	props: {
		scripts: Array,
	},
	data() {
		return {
			count: 0,
		};
	},
	created() {
		console.log(this.scripts);
	},
};
</script>

<style lang="scss">
.bb-right-side {
	position: relative;
	width: 100%;
	height: 100%;
}
.text-btn {
	position: absolute;
	bottom: 2rem;
	left: 75%;
	width: 6.5rem;
	height: 6.5rem;
	margin-left: -3.25rem;
}
.bb-left-btn {
	border: none;
	border-radius: 50%;
	width: 3rem;
	height: 3rem;
	margin-right: 0.5rem;
	font-size: 1.5rem;
	background: black;
	color: white;
	cursor: pointer;
}
.bb-right-btn {
	border: none;
	border-radius: 50%;
	width: 3rem;
	height: 3rem;
	font-size: 1.5rem;
	background: black;
	color: white;
	cursor: pointer;
}
.bb-disabled {
	display: none;
}
.bb-abled {
	display: block;
}
</style>
