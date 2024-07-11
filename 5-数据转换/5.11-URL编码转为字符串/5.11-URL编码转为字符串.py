from urllib.parse import unquote

content = '{"status":0,"require_snr":0,"err_msg":"","logid":"4f04ee45-0b47-11ee-aa78-2af8bc69b01c","err_no":0,' \
          '"datasets":[{"directive":{"header":{' \
          '"dialogRequestId":"dialogRequestId_4f04f0b0-0b47-11ee-b522-2af8bc69b01c",' \
          '"namespace":"ai.dueros.device_interface.screen","name":"RenderVoiceInputText",' \
          '"messageId":"1686811139_388fp6yvy"},"payload":{"rolling":false,"text":"\u518d\u753b\u4e00\u6b21",' \
          '"type":"FINAL"}}},{"directive":{"header":{' \
          '"dialogRequestId":"dialogRequestId_4f04f0b0-0b47-11ee-b522-2af8bc69b01c",' \
          '"namespace":"ai.dueros.device_interface.extensions.iov_task","name":"CreateTask",' \
          '"messageId":"MWQzZDIxN2QtOGM1Yy0xOTFlLTg0NmItZjgxZjI2NjMyOTQ1Kw=="},"payload":{' \
          '"name":"1d3d217d-8c5c-191e-846b-f81f26632945"}}},{"directive":{"header":{' \
          '"dialogRequestId":"dialogRequestId_4f04f0b0-0b47-11ee-b522-2af8bc69b01c",' \
          '"namespace":"ai.dueros.device_interface.app","name":"LaunchApp",' \
          '"messageId":"MWQzZDIxN2QtOGM1Yy0xOTFlLTg0NmItZjgxZjI2NjMyOTQ1Kw=="},"payload":{' \
          '"packageName":"com.baidu.ernie.car",' \
          '"deepLink":"/pages/aigc/index?category=%E5%86%85%E5%AE%B9%E5%88%9B%E4%BD%9C&description=%E6%8A%8A%E4%BD%A0' \
          '%E7%9A%84%E6%83%B3%E8%B1%A1%E5%8F%98%E6%88%90%E7%B2%BE%E7%BE%8E%E7%94%BB%E4%BD%9C&enter_tts=&hint=%E6%89' \
          '%8B%E6%8D%A7%E9%B2%9C%E8%8A%B1%E7%9A%84%E5%B0%91%E5%A5%B3%2F%E6%97%8B%E8%BD%AC%E6%9C%A8%E9%A9%AC%E6%97%81' \
          '%E6%94%BE%E7%9D%80%E5%8F%AF%E7%88%B1%E7%9A%84%E4%B9%A6%E5%8C%85%2F%E5%B8%AE%E6%88%91%E7%94%BB%E4%B8%80%E6' \
          '%9E%9D%E6%99%B6%E8%8E%B9%E5%89%94%E9%80%8F%E7%9A%84%E7%89%A1%E4%B8%B9%E8%8A%B1%2F%E7%94%BB%E7%89%B5%E7%9D' \
          '%80%E6%89%8B%E7%9A%84%E4%B8%80%E5%8F%AA%E7%8C%AB%E5%92%8C%E4%B8%80%E5%8F%AA%E7%8B%97&input_hint=%E8%AF%B7' \
          '%E5%91%8A%E8%AF%89%E6%88%91%E4%BD%A0%E8%A6%81%E6%8F%8F%E7%BB%98%E7%9A%84%E4%B8%96%E7%95%8C&name=%E7%81%B5' \
          '%E6%84%9F%E7%BB%98%E7%94%BB&name_alias=%E7%81%B5%E6%84%9F%E7%94%BB%E7%94%BB%2F%E7%94%BB%E7%94%BB%2F%E7%94' \
          '%BB%E5%9B%BE%2F%E7%94%BB%E4%B8%80%E5%B9%85%E7%94%BB%2F%E7%94%BB%E4%B8%80%E5%B9%85%E5%9B%BE%2F%E7%94%BB%E4' \
          '%B8%80%E5%BC%A0%E7%94%BB%2F%E7%94%BB%E4%B8%80%E5%BC%A0%E5%9B%BE%2F%E7%94%BB%E5%BC%A0%E7%94%BB%2F%E7%94%BB' \
          '%E5%BC%A0%E5%9B%BE%2F%E7%94%BB%E4%B8%AA%E7%94%BB%2F%E7%94%BB%E4%B8%AA%E5%9B%BE%2F%E7%BB%98%E7%94%BB%2F%E7' \
          '%BB%98%E5%9B%BE%2F%E4%BD%9C%E5%9B%BE%2F%E4%BD%9C%E7%94%BB%2F%E5%88%9B%E4%BD%9C%E7%BB%98%E7%94%BB%2F%E5%88' \
          '%9B%E4%BD%9C%E7%BB%98%E5%9B%BE%2FAI%E7%94%BB%E5%9B%BE%2FAI%E7%BB%98%E5%9B%BE%2FAI%E7%BB%98%E7%94%BB%2F%E5' \
          '%B0%8F%E5%BA%A6%E7%94%BB%E7%94%BB%2F%E5%B0%8F%E5%BA%A6%E7%BB%98%E7%94%BB%2Fai%E7%94%BB%E5%9B%BE%2Fai%E7%BB' \
          '%98%E5%9B%BE%2Fai%E7%BB%98%E7%94%BB&options=%7B%22share%22%3Atrue%2C%22share_text_from%22%3A' \
          '%22moments_text%22%7D&result_tts=%E4%BB%A5%E4%B8%8B%E6%98%AF%E6%88%91%E5%B8%AE%E4%BD%A0%E7%94%9F%E6%88%90' \
          '%E7%9A%84%E7%94%BB%E4%BD%9C%E5%93%A6&type=inspired_painting",' \
          '"appName":"lcoPMpPxuN5MVLb0f27vjNoU20o1Q4LD"}}}]}'

encoded_url = content
decoded_url = unquote(encoded_url)

print(decoded_url)
