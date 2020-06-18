
module.exports = {
  "globalSetup": "jest-environment-puppeteer/setup",
  "globalTeardown": "jest-environment-puppeteer/teardown",
  "testEnvironment": "./puppeteer_environment.js",
  'setupFilesAfterEnv': ['./jest.setup.js'],
  

  roots:[
    "<rootDir>"
  ],
  "moduleFileExtensions": [
    "ts",
    "js",
  ],
  // 匹配__tests__文件夹下的后缀为 .test.ts文件
  "testMatch": [
    "**/*.test.*"
  ],
  "transform": {
    "^.+\\.ts$": "ts-jest"
  }
  
};