curl -s "https://api.github.com/users/computervisioneng/repos?per_page=100&type=public" \
  | jq -r '.[].clone_url' \
  | xargs -L1 git clone
