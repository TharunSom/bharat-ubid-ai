def generate_ubid(groups):
  ubid_map={}
  count=1
  for group in groups:
    ubid=f"KA-BIZ-{count:05d}"
    for index in group:
      ubid_map[index]=ubid
      count+=1
  return ubid_map
