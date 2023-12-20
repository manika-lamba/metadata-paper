import csv

multiple_abstracts = [
    "Information Services and Staff-Users Communication in Academic Libraries",
    "Authormagic: a Concept for Author Disambiguation in Large-Scale Digital Libraries",
    "Online Cataloging Automation for Digital Libraries"
]

def text_to_csv(inputFile, outFilePath):
    new_entry_delimiter = "____________________________________________________________"
    author_header = "Author"
    publication_info_header = "Publication info"
    abstract_header = "Abstract"
    link_header = "Links"
    business_indexing_term_header = "Business indexing term"
    subject_header = "Subject"
    classification_header = "Classification"
    identifier_header = "Identifier / keyword"
    title_header = "Title"
    pages_header = "Number of pages"
    degree_date_header = "Degree date"
    school_code_header = "School code"
    source_header = "Source"
    place_of_publication_header = "Place of publication"
    country_of_publication_header = "Country of publication"
    isbn_header = "ISBN"
    advisor_header = "Advisor"
    committee_header = "Committee member"
    univ_header = "University/institution"
    dept_header = "Department"
    univ_loc_header = "University location"
    degree_header = "Degree"
    source_type_header = "Source type"
    language_header = "Language"
    document_type_header = "Document type"
    dis_number_header = "Dissertation/thesis number"
    proQuest_header = "ProQuest document ID"
    document_url_header = "Document URL"
    copyright_header = "Copyright"
    database_header = "Database"
    second_link_header = "Another Link"
    publication_year_header = "Publication year"

    place_of_publication_header_2 = "Placeof publication"
    place_of_publication_header_3 = "Place ofpublication"
    committee_header_2 = "Committeemember"
    country_of_publication_header_2 = "Countryof publication"
    proQuest_header_2 = "ProQuest documentID"
    proQuest_header_3 = "ProQuestdocument ID"
    school_code_header_2 = "Schoolcode"
    school_location_header = "School location"
    country_of_publication_header_3 = "Country ofpublication"
    identifier_header_2 = "Identifier /keyword"
    pages_header_2 = "Numberof pages"
    univ_loc_header_2 = "Universitylocation"
    year_header = "Year"
    url_header = "URL"
    language_header_2 = "Language of publication"


    my_counter = {}
    all_rows = []
    row_headers = [title_header, author_header, publication_info_header, abstract_header, link_header,
                   business_indexing_term_header, subject_header,
                   classification_header, identifier_header, pages_header, degree_date_header,
                   school_code_header, source_header, place_of_publication_header, country_of_publication_header,
                   isbn_header, advisor_header, committee_header, univ_header, dept_header, univ_loc_header,
                   degree_header, source_type_header, language_header, document_type_header, dis_number_header,
                   proQuest_header, document_url_header, copyright_header, database_header, second_link_header,
                   publication_year_header]
    with open(inputFile) as reader:
        content = reader.readlines()
        single_row = {}
        for line in content:
            line = (str(line)).strip()
            if line == "" or line.isspace():
                continue
            if line == new_entry_delimiter:
                all_rows.append(single_row.copy())
                single_row = {}
                continue
            if line.startswith(author_header):
                single_row[author_header] = line[len(author_header) + 2:].strip()
            elif line.startswith(publication_info_header):
                single_row[publication_info_header] = line[len(publication_info_header) + 2:].strip()
            elif line.startswith(abstract_header):
                single_row[abstract_header] = line[len(abstract_header) + 2:].strip()
            elif line.startswith(link_header):
                single_row[link_header] = line[len(link_header) + 2:].strip()
            elif line.startswith(business_indexing_term_header):
                single_row[business_indexing_term_header] = line[len(business_indexing_term_header) + 2:].strip()
            elif line.startswith(subject_header):
                single_row[subject_header] = line[len(subject_header) + 2:].strip()
            elif line.startswith(classification_header):
                single_row[classification_header] = line[len(classification_header) + 2:].strip()
            elif line.startswith(identifier_header):
                single_row[identifier_header] = line[len(identifier_header) + 2:].strip()
            elif line.startswith(identifier_header_2):
                single_row[identifier_header] = line[len(identifier_header_2) + 2:].strip()
            elif line.startswith(title_header):
                temp_title = line[len(title_header) + 2:].strip()
                if temp_title.startswith('"') and temp_title.endswith('"'):
                    temp_title = temp_title[1:-1]
                if temp_title.startswith('\'') and temp_title.endswith('\''):
                    temp_title = temp_title[1:-1]
                single_row[title_header] = temp_title
            elif line.startswith(pages_header):
                single_row[pages_header] = line[len(pages_header) + 2:].strip()
            elif line.startswith(pages_header_2):
                single_row[pages_header] = line[len(pages_header_2) + 2:].strip()
            elif line.startswith(degree_date_header):
                single_row[degree_date_header] = line[len(degree_date_header) + 2:].strip()
            elif line.startswith(school_code_header):
                single_row[school_code_header] = line[len(school_code_header) + 2:].strip()
            elif line.startswith(source_type_header):
                single_row[source_type_header] = line[len(source_type_header) + 2:].strip()
            elif line.startswith(source_header):
                single_row[source_header] = line[len(source_header) + 2:].strip()
            elif line.startswith(place_of_publication_header):
                single_row[place_of_publication_header] = line[len(place_of_publication_header) + 2:].strip()
            elif line.startswith(country_of_publication_header):
                single_row[country_of_publication_header] = line[len(country_of_publication_header) + 2:].strip()
            elif line.startswith(isbn_header):
                single_row[isbn_header] = line[len(isbn_header) + 2:].strip()
            elif line.startswith(advisor_header):
                single_row[advisor_header] = line[len(advisor_header) + 2:].strip()
            elif line.startswith(committee_header):
                single_row[committee_header] = line[len(committee_header) + 2:].strip()
            elif line.startswith(univ_header):
                single_row[univ_header] = line[len(univ_header) + 2:].strip()
            elif line.startswith(dept_header):
                single_row[dept_header] = line[len(dept_header) + 2:].strip()
            elif line.startswith(univ_loc_header):
                single_row[univ_loc_header] = line[len(univ_loc_header) + 2:].strip()
            elif line.startswith(univ_loc_header_2):
                single_row[univ_loc_header] = line[len(univ_loc_header_2) + 2:].strip()
            elif line.startswith(degree_header):
                single_row[degree_header] = line[len(degree_header) + 2:].strip()
            elif line.startswith(language_header):
                if line.startswith(language_header_2):
                    single_row[language_header] = line[len(language_header_2) + 2:].strip()
                else:
                    single_row[language_header] = line[len(language_header) + 2:].strip()
            elif line.startswith(document_type_header):
                single_row[document_type_header] = line[len(document_type_header) + 2:].strip()
            elif line.startswith(dis_number_header):
                single_row[dis_number_header] = line[len(dis_number_header) + 2:].strip()
            elif line.startswith(proQuest_header):
                single_row[proQuest_header] = line[len(proQuest_header) + 2:].strip()
            elif line.startswith(document_url_header):
                single_row[document_url_header] = line[len(document_url_header) + 2:].strip()
            elif line.startswith(url_header):
                single_row[document_url_header] = line[len(url_header) + 2:].strip()
            elif line.startswith(copyright_header):
                single_row[copyright_header] = line[len(copyright_header) + 2:].strip()
            elif line.startswith(database_header):
                single_row[database_header] = line[len(database_header) + 2:].strip()
            elif line.startswith("https://"):
                single_row[second_link_header] = line.strip()
            elif line.startswith(publication_year_header):
                single_row[publication_year_header] = line[len(publication_year_header) + 2:].strip()
            elif line.startswith(year_header):
                single_row[publication_year_header] = line[len(year_header) + 2:].strip()
            elif line.startswith(place_of_publication_header_2):
                single_row[place_of_publication_header] = line[len(place_of_publication_header_2) + 2:].strip()
            elif line.startswith(place_of_publication_header_3):
                single_row[place_of_publication_header] = line[len(place_of_publication_header_3) + 2:].strip()
            elif line.startswith(committee_header_2):
                single_row[committee_header] = line[len(committee_header_2) + 2:].strip()
            elif line.startswith(country_of_publication_header_2):
                single_row[country_of_publication_header] = line[len(country_of_publication_header_2) + 2:].strip()
            elif line.startswith(country_of_publication_header_3):
                single_row[country_of_publication_header] = line[len(country_of_publication_header_3) + 2:].strip()
            elif line.startswith(proQuest_header_2):
                single_row[proQuest_header] = line[len(proQuest_header_2) + 2:].strip()
            elif line.startswith(proQuest_header_3):
                single_row[proQuest_header] = line[len(proQuest_header_3) + 2:].strip()
            elif line.startswith(school_code_header_2):
                single_row[school_code_header] = line[len(school_code_header_2) + 2:].strip()
            elif line.startswith(school_location_header):
                single_row[univ_loc_header] = line[len(school_location_header) + 2:].strip()
            else:
                if ":" in line:
                    prefix = line.split(":")[0]
                    if prefix in my_counter:
                        my_counter[prefix] = my_counter[prefix] + 1
                    else:
                        my_counter[prefix] = 1
    print "========Some keys=========="
    for key, val in my_counter.items():
        if val > 2:
            print key
    print "========Some keys=========="

    #######
    alternate_abstract_header = "Alternate abstract:"
    for idx, one_row in enumerate(all_rows):
        found = False
        if not bool(one_row):
            continue
        if title_header not in one_row:
            continue
        idx = one_row[abstract_header].find(alternate_abstract_header)
        if idx != -1:
            for multiple_abstracts_title in multiple_abstracts:
                if one_row[title_header].startswith(multiple_abstracts_title):
                    found = True
                    break
            if found:
                start_idx = idx + 20
                end_idx = len(one_row[abstract_header])
                one_row[abstract_header] = one_row[abstract_header][start_idx:end_idx]
            else:
                print("Should not come here")
                start_idx = 0
                end_idx = idx -1
                one_row[abstract_header] = one_row[abstract_header][start_idx:end_idx]
    #######

    unique_title = set()
    with open(outFilePath, mode='wb') as out_file:
        all_writer = csv.writer(out_file, delimiter=',')
        all_writer.writerow(row_headers)
        for one_row in all_rows:
            put_row = []
            for one_row_header in row_headers:
                put_row.append(one_row.get(one_row_header, ""))
            write_title = str(put_row[0]).strip().lower()
            if write_title not in unique_title:
                unique_title.add(write_title)
                all_writer.writerow(put_row)


if __name__ == "__main__":
    inputFile = "\\07_jan_2022\\data\\695-fulltext-2021-11-30.txt"
    outputFile = "\\07_jan_2022\\data\\csv_695-fulltext-2021-11-30.csv"
    text_to_csv(inputFile, outputFile)
