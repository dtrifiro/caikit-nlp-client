/^import / && ($2 ~ /^caikit_data_model.*/ || $2 ~ /^caikit.*/) {
    $2 = "caikit_nlp_client.generated."$2
}
/^from / && ($2 ~ /^caikit_data_model.*/ || $2 ~ /^caikit.*/) {
    $2 = "caikit_nlp_client.generated."$2
}
1