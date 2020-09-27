import Vue from 'vue';
import VueRouter from 'vue-router';
// import StoryPage from '@/views/StoryPage.vue';

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
		path: '/story/:storyId/review/:myStoryId',
		name: 'finishedStory',
		props: route => ({
			storyId: Number(route.params.storyId),
			myStoryId: Number(route.params.myStoryId),
		}),
		component: () => import('@/views/story/StoryFinishedPage.vue'),
	},
	{
		path: '/story/:storyId/:myStoryId',
		name: 'story',
		props: route => ({
			storyId: Number(route.params.storyId),
			myStoryId: Number(route.params.myStoryId),
		}),
		component: () => import('@/views/story/StoryPage.vue'),
	},
	{
		path: '/bookshelf',
		name: 'bookshelf',
		component: () => import('@/views/BookshelfPage.vue'),
	},
	{
		path: '/bookshelf/:storyId',
		name: 'storybook',
		component: () => import('@/views/story/StoryBookPage.vue'),
	},
	{
		path: '/profile',
		name: 'profile',
		component: () => import('@/views/profile/ProfilePage.vue'),
	},
	{
		path: '/profile/modifyinfo',
		name: 'modifyinfo',
		component: () => import('@/views/profile/ModifyInfoPage.vue'),
	},
	{
		path: '*',
		redirect: '/404',
	},
	{
		path: '/404',
		component: () => import('@/views/NotFoundPage.vue'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
