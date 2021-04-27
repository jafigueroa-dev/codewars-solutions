function domainName(url){
  return url.replace(/https|http|www|\.|\:/g, "//").split("//").filter(n => n)[0]
}