def calculate_coverage(test_cases, edge_cases):
    required_categories = {
        "Positive",
        "Negative",
        "Boundary",
        "Security",
        "Performance",
        "Concurrency",
        "Accessibility"
    }

    found_categories = {tc.type for tc in test_cases}
    missing_categories = required_categories - found_categories

    # edge case checks
    edge_requirements = {
        "security": any("security" in e.lower() for e in edge_cases),
        "concurrency": any("concurr" in e.lower() for e in edge_cases),
        "performance": any("performance" in e.lower() or "load" in e.lower() for e in edge_cases),
        "validation": any("validation" in e.lower() or "invalid" in e.lower() for e in edge_cases),
        "accessibility": any("accessibility" in e.lower() for e in edge_cases),
    }

    edge_missing = [k for k, v in edge_requirements.items() if not v]

    # simple scoring
    category_score = len(found_categories) / len(required_categories)
    edge_score = (len(edge_requirements) - len(edge_missing)) / len(edge_requirements)

    overall_score = round((category_score * 0.6 + edge_score * 0.4), 2)

    return {
        "categories_covered": list(found_categories),
        "missing_categories": list(missing_categories),
        "missing_edge_case_types": edge_missing,
        "coverage_score": overall_score
    }
