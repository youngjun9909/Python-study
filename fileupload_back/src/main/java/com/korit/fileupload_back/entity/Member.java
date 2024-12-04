package com.korit.fileupload_back.entity;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Data
@Builder
public class Member {
    private Long id;
    private String name;
    private String profileImgPath;
}
