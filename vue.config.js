const proxyObj = {}
proxyObj['/api'] = {
  target: 'http://localhost:5000',
  changeOrigin: true,
  pathRewrite: {
    '^api/': ''
  }
}
module.exports = {
  devServer: {
    host: 'localhost',
    port: 8080,
    proxy: proxyObj
  }
}