<template>
  <section class="todo-input">
    <input
      type="text"
      placeholder="请输入代办事项"
      v-model="text"
      v-on:input=inputText
      v-on:keyup.enter="addItem"
    />
    <button v-on:click=addItem>添加</button>
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
      if (e.target.value != "") {
        this.inputArry = [{"name":e.target.value}]
      }
      
    },
    addItem() {
      if (this.inputArry != "") {
        this.$store.dispatch("addItem", this.inputArry);
        this.inputArry = "";
        this.text = "";
      }
    },
  },
};
</script>