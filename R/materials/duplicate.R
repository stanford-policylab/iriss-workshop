has_duplicate <- function(v) {
    any(duplicated(v))
}

num_duplicates <- function(v) {
    sum(duplicated(v))
}