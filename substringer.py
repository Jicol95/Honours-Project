from suffix_trees import STree

# Hard coded test case for this script represents 2 scores contour_abstract
a = ["+++0000+-+-0","+-+0+++0-+-00000","+-+-+00+++-0-0000"]
aMaster = a
# It is crucial that they are sorted longest to shortest
a = sorted(a,key=len, reverse=True)
# Build a genralised suffix tree with a
st = STree.STree(a)
# Instantiate list that will contain common patterns
matches = []
queue = []

while st.lcs() != "":
    # If there is nothing in the queue
    if not queue:
        # Find the longest common sub_string
        longest_common_substring = st.lcs()
        lcs_start = a[0].find(longest_common_substring)
        lcs_end = lcs_start + len(longest_common_substring)
    elif queue:
        longest_common_substring = queue.pop(0)
        lcs_start = aMaster[0].find(longest_common_substring)
        lcs_end = lcs_start + len(longest_common_substring)

    # If the longest common substring isnt in the list of matches then add it
    if not any([(longest_common_substring in match) for match in matches]):
        matches.append(longest_common_substring)
        lookback = list(longest_common_substring)

        # Go through and redact the match left to right one char at a time checking
        # if a new longest common substring has been forced
        for i in range(lcs_start, lcs_end):
            TEMP = list(a[0])
            TEMP[i] = 'x'
            a[0] = "".join(TEMP)
            st = STree.STree(a)
            if st.lcs() != longest_common_substring and st.lcs() not in queue and st.lcs not in matches:
                queue.append(st.lcs())

        # Remove the redaction one char at a time left to right
        lookback = list(longest_common_substring)
        for i in range(lcs_start,lcs_end):
            TEMP = list(a[0])
            TEMP[i] = lookback.pop(0)
            a[0] = "".join(TEMP)
            st = STree.STree(a)
            if st.lcs() != longest_common_substring and st.lcs() not in queue and st.lcs not in matches:
                queue.append(st.lcs())

            redaction = 'x' * len(longest_common_substring)
            # Redact the string
            a[0] = a[0].replace(longest_common_substring, redaction,1)

        # Remove the redaction one char at a time right to left
        lookback = list(longest_common_substring)
        for i in range(lcs_end-1,lcs_start-1, -1):
            TEMP = list(a[0])
            TEMP[i] = lookback.pop()
            a[0] = "".join(TEMP)
            st = STree.STree(a)
            if st.lcs() != longest_common_substring and st.lcs() not in queue and st.lcs not in matches:
                queue.append(st.lcs())

        redaction = 'x' * len(longest_common_substring)
        # Redact the string
        a[0] = a[0].replace(longest_common_substring, redaction,1)

    if not(lookback) and not(queue):
        break
print(matches)



# for i in range(0,len(a[0])):
#     longest_common_substring = st.lcs()
#     # lcs_start = a[0].find(longest_common_substring)
#     # lcs_end = lcs_start + len(longest_common_substring)
#     if i != 0:
#         TEMP = list(a[0])
#         TEMP[i-1] = lookback
#         a[0] = "".join(TEMP)
#
#     lookback = a[0][i]
#     a[0] = list(a[0])
#     a[0][i] = 'x'
#     a[0] = "".join(a[0])
#     st = STree.STree(a)
#
#     print(matches)
#
#     if not any([(longest_common_substring in match) for match in matches]):
#         matches.append(longest_common_substring)




# # For the length of the fisrt string in list a
# for i in range(0,len(a[0])):
#     # Find the longest shared substring between all elements of a
#     longest_common_substring = st.lcs()
#     # If it returns empty string then exit the loop
#     if longest_common_substring == "":
#         break
#     # Get the start index of longest common sub_string
#     lcs_start = a[0].find(longest_common_substring)
#     # Get the end index by adding the lenght of the sub_string to the start indexs
#     lcs_end = lcs_start + len(longest_common_substring)
#     # Generate enough x's to redaxt the string ensuring the same string at that positions
#     # wont trigger another match
#     redaction = 'x' * len(longest_common_substring)
#     # Redact the string
#     a[0] = a[0].replace(longest_common_substring, redaction)
#     # Rebuild the tree now that the first element of list a has been partially redacted
#     st = STree.STree(a)
#     # Add the longest common substring to the list of matches
#     matches.append(longest_common_substring)
# print(matches)
