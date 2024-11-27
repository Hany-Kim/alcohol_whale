<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="navbar">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          icon="menu"
          id="menuButton"
          :disabled="!isLoggedIn()"
        />

        <q-toolbar-title>
          <router-link to="/" class="home-link" v-if="isLoggedIn()">술고래 매장 관리</router-link>
          <span v-else class="home-link">술고래 매장 관리</span>
        </q-toolbar-title>

        <q-input dark dense standout v-model="searchText" input-class="text-right" class="q-ml-md" @keyup.enter="searchText = ''">
          <template v-slot:append>
            <q-icon v-if="searchText === ''" name="search" />
            <q-icon v-else name="clear" class="cursor-pointer" @click="searchText = ''" />
          </template>
        </q-input>
        <span class="q-mx-sm">
          매장 이름
          <q-tooltip color="black">개인 정보</q-tooltip>
        </span>
          
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      overlay
      bordered
      class="bg-grey-2"
    >
      <q-list>
        <q-item-label header class="row justify-between items-center">
          <span class="text-weight-bold">메뉴</span>
          <q-icon name="close" size="1.5rem" color="dark" @click="leftDrawerOpen = !leftDrawerOpen"/>
        </q-item-label>
        <q-item clickable tag="a" router-link to="/">
          <q-item-section avatar>
            <q-icon name="text_snippet" />
          </q-item-section>
          <q-item-section>
            <q-item-label>DATABASE</q-item-label>
            <q-item-label caption>주류 재고 데이터 관리</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable tag="a" router-link to="/analysis">
          <q-item-section avatar>
            <q-icon name="analytics" />
          </q-item-section>
          <q-item-section>
            <q-item-label>ANALYTIC</q-item-label>
            <q-item-label caption>데이터 분석</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable tag="a" router-link to="/request">
          <q-item-section avatar>
            <q-icon name="outgoing_mail" />
          </q-item-section>
          <q-item-section>
            <q-item-label>REQUEST</q-item-label>
            <q-item-label caption>요청 보내기</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable @click="logout()">
          <q-item-section avatar>
            <q-icon name="logout" color="red" />
          </q-item-section>
          <q-item-section>
            <q-item-label>LOGOUT</q-item-label>
            <q-item-label caption>로그아웃</q-item-label>
          </q-item-section>
        </q-item>        
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style scoped>
  @font-face {
    font-family: 'MaruBuri';
    font-weight: 400; 
    font-style: normal; 
    src: url(https://cdn.jsdelivr.net/gh/webfontworld/naver/MaruBuri-Regular.woff2) format('woff2');
    font-display: swap;
  }
 template{font-family: 'MaruBuri';}
  .home-link {
    color: white;
    text-decoration: none;
    transition: .3s;
  }

  .home-link:hover {
    color: #F0C2C2;
  }

  .navbar {
    background-color: #203864;
    font-family: 'MaruBuri';
  }


</style>

<script>
  import router from '@/router'
  import { ref, computed } from 'vue'
  import { useStore, mapActions, mapGetters } from 'vuex'

  export default {
    name: 'MainTemplate',
    setup () {

      const store = useStore()
      const isLoggedIn = computed(() => store.getters.isLoggedIn)

      if (!isLoggedIn.value) {
        router.push({ name: 'login' })
      }

      return {
        leftDrawerOpen: ref(false),
        searchText: ref(''),
        ...mapGetters(['isLoggedIn']),
        ...mapActions(['logout']),
      }
    },
  }
</script>
