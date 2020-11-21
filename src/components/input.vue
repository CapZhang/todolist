<template>
  <section class="todo-input">
    <input
      type="text"
      placeholder="请输入代办事项"
      v-model="text"
      v-on:input="inputText"
    />
    <button v-on:click="addItem">添加</button>
  </section>
</template>

<script>
export default {
  data() {
    return {
      text: "",
    };
  },
  methods: {
    inputText(e) {
      this.text = e.target.value;
    },
    addItem() {
      this.$store.dispatch("addItem", this.text);
      this.text = "";
    },
  },
};
</script>