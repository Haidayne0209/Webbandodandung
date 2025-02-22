﻿$(document).ready(function () {
    "use strict";
    $("#account-datatable").DataTable({
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>",
            },
            info: "Showing customers _START_ to _END_ of _TOTAL_",
            lengthMenu:
                `Hiển thị <select class='form-select form-select-sm ms-1 me-1'>
                                <option value="10">10</option>
                                <option value="20">20</option>
                                <option value="-1">All</option>
                        </select>`,
        },
        columnDefs: [{targets: -1, className: "dt-body-right"}],
        pageLength: 10,
        columns: [
            {orderable: !0,},
            {orderable: !0},
            {orderable: !0},
            {orderable: !0},
            {orderable: !0},
            {orderable: !0},
            {orderable: !1},
        ],
        select: {style: "multi"},
        order: [[0, "asc"]],
        drawCallback: function () {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded"),
                $("#products-datatable_length label").addClass("form-label"),
                document
                    .querySelector(".dataTables_wrapper .row")
                    .querySelectorAll(".col-md-6")
                    .forEach(function (e) {
                        e.classList.add("col-sm-6"),
                            e.classList.remove("col-sm-12"),
                            e.classList.remove("col-md-6");
                    });
        },
    });
});
