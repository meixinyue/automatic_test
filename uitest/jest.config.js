
module.exports = {
  "globalSetup": "jest-environment-puppeteer/setup",
  "globalTeardown": "jest-environment-puppeteer/teardown",
  "testEnvironment": "./puppeteer_environment.js",
  'setupFilesAfterEnv': ['./jest.setup.js'],//设置timeout时间
  

  roots:[
    "<rootDir>"
  ],
  "moduleFileExtensions": [
    "ts",
    "js",
  ],
  // 匹配__tests__文件夹下的后缀为 .test.的所有文件
  "testMatch": [
    "**/*.test.*"
  ],
  "transform": {
    "^.+\\.ts$": "ts-jest"
  }
  
};