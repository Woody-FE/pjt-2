import Vue from 'vue';
import VueRouter from 'vue-router';
import StoryPage from '@/views/StoryPage.vue';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'main',
		component: () => import('@/views/MainPage.vue'),
	},
	{
		path: '/guide',
		name: 'guide',
		component: () => import('@/views/GuidePage.vue'),
	},
	{
		path: '/login',
		name: 'login',
		component: () => import('@/views/LoginPage.vue'),
	},
	{
		path: '/signup',
		name: 'signup',
		component: () => import('@/views/SignupPage.vue'),
	},
	{
		path: '/story/:pk',
		name: 'story',
		props: route => ({
			pk: Number(route.params.pk),
		}),
		// component: () => import('@/views/StoryPage.vue'),
		component: StoryPage,
	},
	{
		path: '/bookshelf',
		name: 'bookshelf',
		component: () => import('@/views/BookshelfPage.vue'),
	},
	{
		path: '/profile/:userid',
		name: 'profile',
		component: () => import('@/views/profile/ProfilePage.vue'),
		props: route => ({
			userId: Number(route.params.userid),
		}),
	},
	{
		path: '/profile/:userid/modifyinfo',
		name: 'modifyinfo',
		component: () => import('@/views/profile/ModifyInfoPage.vue'),
		props: route => ({
			userId: Number(route.params.userid),
		}),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
