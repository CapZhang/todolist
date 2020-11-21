<template>
  <section>
    <ul class="todo-list" v-show="list.length">
      <li
        class="todo-item"
        v-for="(item, index) in list"
        v-bind:key="index + item"
      >
        <span>{{ index + 1 }}.</span>
        <p>{{ item }}</p>
        <button @click="removeItem(index)">完成</button>
      </li>
    </ul>
    <div class="todo-nodata" v-show="!list.length">
      恭喜你完成所有内容，请继续添加！！
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      list: this.$store.state.list,
    };
  },

  methods: {
    removeItem(index) {
      this.$store.dispatch("removeItem", index);
    },
  },
};
</script>