<template >
  <section class="todo-read">
    <div v-show="readStatusDoing">正在读取...</div>
    <div v-show="!readStatusDoing && is_hiden">读取完成</div>
    <button v-on:click="readJsonDoc">重载</button>
  </section>
</template>

<script>
export default {
  data() {
    return {
      readStatusDoing: true,
      readitemsStr: ["123"],
      temp: [{ name: "吃饭j" }, { name: "睡觉j" }],
      is_run: true,
      is_hiden: true,
    };
  },
  methods: {
    hiden_ele() {
      this.is_hiden = false;
    },
    timer() {
      return setTimeout(() => {
        this.hiden_ele();
      }, 5000);
    },
    readJsonDoc() {
      console.log("++++++++++++++++");
      console.log(this);
      this.$https
        .get("/todo")
        .then(function (res) {
          console.log(res);
          alert(res);
        })
        .catch(function (err) {
          alert(err);
        });
    },
  },
  created () {
    // mounted vue的生命周期钩子，组件加载后使用
     this.readJsonDoc();
      this.readStatusDoing = false;
      this.$store.dispatch("readItems", this.temp);
  },
  watch: {
    readStatusDoing() {
      this.timer();
    },
  },
};
</script>

<style scoped>
</style>