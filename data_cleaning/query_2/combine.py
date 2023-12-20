import csv
import os


def combine_all_files(inputFolderPath, outFilePath):
    order = {}
    headers_in_order = []
    last_num = 0
    all_files = os.listdir(inputFolderPath)
    all_new_rows = []
    for file in all_files:
        with open(inputFolderPath + "//" + file, "r") as dataFile:
            dataFileReader = csv.reader(dataFile, delimiter=',')
            curMap = {}
            isFirst = 0
            for row in dataFileReader:
                new_row = [''] * 17
                for idx, field in enumerate(row):
                    if field is None or str(field) == '' or (str(field)).isspace():
                        continue
                    if isFirst == 0:
                        field = str(field).strip()
                        if (field == 'University/institution' or field == 'University/insitution' or field == 'University'):
                            field = 'University/institution'
                        if (field == 'Dissertation/thesis number' or field == 'Dissertion/thesis number'):
                            field = 'Dissertation/thesis number'
                        if (field == 'Identifier / keyword' or field == 'Identifier/keyword'):
                            field = 'Identifier/keyword'
                        if (field == 'Number of pages' or field == 'Pages'):
                            field = 'Number of pages'
                        if (field == 'Degree date' or field == 'Year'):
                            field = 'Degree date'
                        if (field == 'University location' or field == 'Location'):
                            field = 'University location'
                        if((str(field)).lower() not in order):
                            order[(str(field)).lower()] = last_num
                            headers_in_order.append(str(field))
                            last_num += 1

                        curMap[idx] = (str(field)).lower()
                    else:
                        new_row[order[curMap[idx]]] = field
                isFirst += 1
                all_new_rows.append(new_row)

    with open(outFilePath, mode='wb') as out_file:
        all_writer = csv.writer(out_file, delimiter=',')
        all_writer.writerow(headers_in_order)
        for new_row in all_new_rows:
            if all('' == s or s.isspace() for s in new_row):
                continue
            all_writer.writerow(new_row)


def text_to_csv(inputFile, outFilePath):
    new_entry_delimiter = "____________________________________________________________"
    author_header = "Author"
    publication_info_header = "Publication info"
    abstract_header = "Abstract"
    link_header = "Links"
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
    publication_year = "Publication year"

    place_of_publication_header_2 = "Placeof publication"
    place_of_publication_header_3 = "Place ofpublication"
    committee_header_2 = "Committeemember"

    my_counter = {}
    all_rows = []
    row_headers = [title_header, author_header, publication_info_header, abstract_header, link_header, subject_header,
                   classification_header, identifier_header, pages_header, degree_date_header,
                   school_code_header, source_header, place_of_publication_header, country_of_publication_header,
                   isbn_header, advisor_header, committee_header, univ_header, dept_header, univ_loc_header,
                   degree_header, source_type_header, language_header, document_type_header, dis_number_header,
                   proQuest_header, document_url_header, copyright_header, database_header, second_link_header,
                   publication_year]
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
            elif line.startswith(subject_header):
                single_row[subject_header] = line[len(subject_header) + 2:].strip()
            elif line.startswith(classification_header):
                single_row[classification_header] = line[len(classification_header) + 2:].strip()
            elif line.startswith(identifier_header):
                single_row[identifier_header] = line[len(identifier_header) + 2:].strip()
            elif line.startswith(title_header):
                single_row[title_header] = line[len(title_header) + 2:].strip()
            elif line.startswith(pages_header):
                single_row[pages_header] = line[len(pages_header) + 2:].strip()
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
            elif line.startswith(degree_header):
                single_row[degree_header] = line[len(degree_header) + 2:].strip()
            elif line.startswith(language_header):
                single_row[language_header] = line[len(language_header) + 2:].strip()
            elif line.startswith(document_type_header):
                single_row[document_type_header] = line[len(document_type_header) + 2:].strip()
            elif line.startswith(dis_number_header):
                single_row[dis_number_header] = line[len(dis_number_header) + 2:].strip()
            elif line.startswith(proQuest_header):
                single_row[proQuest_header] = line[len(proQuest_header) + 2:].strip()
            elif line.startswith(document_url_header):
                single_row[document_url_header] = line[len(document_url_header) + 2:].strip()
            elif line.startswith(copyright_header):
                single_row[copyright_header] = line[len(copyright_header) + 2:].strip()
            elif line.startswith(database_header):
                single_row[database_header] = line[len(database_header) + 2:].strip()
            elif line.startswith("https://"):
                single_row[second_link_header] = line.strip()
            elif line.startswith(publication_year):
                single_row[publication_year] = line[len(publication_year) + 2:].strip()
            elif line.startswith(place_of_publication_header_2):
                single_row[place_of_publication_header] = line[len(place_of_publication_header_2) + 2:].strip()
            elif line.startswith(place_of_publication_header_3):
                single_row[place_of_publication_header] = line[len(place_of_publication_header_3) + 2:].strip()
            elif line.startswith(committee_header_2):
                single_row[committee_header] = line[len(committee_header_2) + 2:].strip()
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

def compare(input_file_1, input_file_2, output_file):
    title_set = set()
    with open(input_file_1) as reader_1:
        ground_truth = csv.reader(reader_1, delimiter=',')
        next(ground_truth, None)
        for row_ground_truth in ground_truth:
            title_set.add(str(row_ground_truth[3]).strip().lower())
    found_row = []
    with open(input_file_2) as reader_2:
        extra = csv.reader(reader_2, delimiter=',')
        header_count = 0
        for row_extra in extra:
            if header_count == 0:
                found_row.append(row_extra)
                header_count += 1
                continue
            title = str(row_extra[0]).strip().lower()
            if title not in title_set:
                found_row.append(row_extra)
    with open(output_file, mode='wb') as out_file:
        all_writer = csv.writer(out_file, delimiter=',')
        for one_row in found_row:
            all_writer.writerow(one_row)


if __name__ == "__main__":
    ### Task - 1 Combine all files
    task1_inputFolderPath = "\\18_july_2021\\CSV_1\\1"
    task_1_outFile = "\\18_july_2021\\task_1_output.csv"
    combine_all_files(task1_inputFolderPath, task_1_outFile)

    ### Task -2 Text to csv
    task_2_inputFile = "\\18_july_2021\\phd_text files_combined_22.03.2021.txt"
    task_2_outputFile = "\\18_july_2021\\task_2_output.csv"
    text_to_csv(task_2_inputFile, task_2_outputFile)

    ### Task - 3 Compare
    task_3_outputFile = "\\18_july_2021\\task_3_output.csv"
    compare(task_1_outFile, task_2_outputFile, task_3_outputFile)
