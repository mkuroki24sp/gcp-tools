# gcp-tools
Useful Tools for Google Cloud Platform

## add-multi-iam-policy.py
- GCP上で、指定したユーザーに対して複数プロジェクトに複数の権限を一括で付与するツール
    - プロジェクトと権限はconfig.iniに記載し、ユーザーは引数で指定する

### 実行例
    python ./add-multi-iam-policy.py mkuroki@example.com

上記の実行例では、config.iniに記載している内容が

    [iam-roles-config]
    projects: ["dev001", "stg001", "prod001"]
    roles: ["roles/bigquery.admin", "roles/editor", "roles/logging.configWriter", "roles/logging.logWriter", "roles/logging.viewer"]

だとすると、下記のようなgcloudコマンドが実行される

    gcloud projects add-iam-policy-binding dev001 --member=mkuroki@example.com --role=roles/bigquery.admin
    gcloud projects add-iam-policy-binding dev001 --member=mkuroki@example.com --role=roles/editor
    gcloud projects add-iam-policy-binding dev001 --member=mkuroki@example.com --role=roles/logging.configWriter
    gcloud projects add-iam-policy-binding dev001 --member=mkuroki@example.com --role=roles/logging.logWriter
    gcloud projects add-iam-policy-binding dev001 --member=mkuroki@example.com --role=roles/logging.viewer
    gcloud projects add-iam-policy-binding stg001 --member=mkuroki@example.com --role=roles/bigquery.admin
    gcloud projects add-iam-policy-binding stg001 --member=mkuroki@example.com --role=roles/editor
    gcloud projects add-iam-policy-binding stg001 --member=mkuroki@example.com --role=roles/logging.configWriter
    gcloud projects add-iam-policy-binding stg001 --member=mkuroki@example.com --role=roles/logging.logWriter
    gcloud projects add-iam-policy-binding stg001 --member=mkuroki@example.com --role=roles/logging.viewer
    gcloud projects add-iam-policy-binding prod001 --member=mkuroki@example.com --role=roles/bigquery.admin
    gcloud projects add-iam-policy-binding prod001 --member=mkuroki@example.com --role=roles/editor
    gcloud projects add-iam-policy-binding prod001 --member=mkuroki@example.com --role=roles/logging.configWriter
    gcloud projects add-iam-policy-binding prod001 --member=mkuroki@example.com --role=roles/logging.logWriter
    gcloud projects add-iam-policy-binding prod001 --member=mkuroki@example.com --role=roles/logging.viewer

### 次やりたいこと
dryrunオプションを書きたかったが、時間が足りなかったので一旦ここまで
