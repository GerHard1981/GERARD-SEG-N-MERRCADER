def check_feature_license(feature: str) -> bool:
    return feature in {"core", "analysis", "cloud"}
